"""
Script: ambil_frekuensi.py
Fungsi: Ambil tabel frekuensi produk dan frequent itemsets
        untuk keperluan pengisian Bab 4 skripsi
"""

import pandas as pd
import mysql.connector
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder

# ============================================================
# KONFIGURASI - sesuaikan dengan MySQL kamu
# ============================================================
DB_CONFIG = {
    'host'    : 'localhost',
    'user'    : 'root',
    'password': 'error1234',         
    'database': 'db_fpgrowth'
}

# Filter tahun berapa yang mau ditampilkan (contoh: 2019)
TAHUN      = 2022       
MIN_SUPPORT = 0.01  # 1%
TOP_N       = 10    # ambil 10 teratas
# ============================================================


def main():
    # Koneksi ke MySQL
    conn   = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    print(f"\n{'='*60}")
    print(f"  DATA TAHUN {TAHUN}")
    print(f"{'='*60}")

    # Ambil data transaksi sesuai tahun
    cursor.execute("""
        SELECT no_invoice, nama_produk
        FROM transaksi
        WHERE YEAR(tanggal_transaksi) = %s
        ORDER BY no_invoice
    """, (TAHUN,))

    rows = cursor.fetchall()
    df   = pd.DataFrame(rows, columns=['no_invoice', 'nama_produk'])

    print(f"\nTotal baris data tahun {TAHUN}: {len(df)}")
    print(f"Total transaksi (no_invoice unik): {df['no_invoice'].nunique()}")

    # ── TABEL 1: FREKUENSI PRODUK ──
    print(f"\n{'─'*60}")
    print(f"  TABEL FREKUENSI PRODUK (Top {TOP_N})")
    print(f"{'─'*60}")

    frekuensi_produk = df['nama_produk'].value_counts().reset_index()
    frekuensi_produk.columns = ['Nama Produk', 'Jumlah Frekuensi']

    print(frekuensi_produk.head(TOP_N).to_string(index=False))

    # ── TABEL 2: FREQUENT ITEMSETS ──
    print(f"\n{'─'*60}")
    print(f"  TABEL FREQUENT ITEMSETS (Min Support {MIN_SUPPORT*100}%, Top {TOP_N})")
    print(f"{'─'*60}")

    # Bentuk basket (itemset per transaksi)
    basket = df.groupby('no_invoice')['nama_produk'].apply(list).tolist()
    basket = [list(set(items)) for items in basket if len(set(items)) > 1]

    print(f"Transaksi dengan >1 produk: {len(basket)}")

    # TransactionEncoder
    te       = TransactionEncoder()
    te_array = te.fit(basket).transform(basket)
    df_enc   = pd.DataFrame(te_array, columns=te.columns_)

    # FP-Growth
    frequent_itemsets = fpgrowth(df_enc, min_support=MIN_SUPPORT, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(len)

    # Filter hanya itemsets dengan 2+ produk (untuk asosiasi)
    fi_multi = frequent_itemsets[frequent_itemsets['length'] >= 2].copy()
    fi_multi = fi_multi.sort_values('support', ascending=False)

    # Format tampilan
    fi_multi['Nama Produk']       = fi_multi['itemsets'].apply(lambda x: ' & '.join(sorted(x)))
    fi_multi['Jumlah Frekuensi']  = (fi_multi['support'] * len(basket)).round(0).astype(int)
    fi_multi['Support (%)']       = (fi_multi['support'] * 100).round(2)

    print(fi_multi[['Nama Produk', 'Jumlah Frekuensi', 'Support (%)']].head(TOP_N).to_string(index=False))

    # ── EXPORT KE EXCEL ──
    output_file = f'frekuensi_{TAHUN}.xlsx'
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        frekuensi_produk.head(TOP_N).to_excel(
            writer, sheet_name='Frekuensi Produk', index=False)
        fi_multi[['Nama Produk', 'Jumlah Frekuensi', 'Support (%)']].head(TOP_N).to_excel(
            writer, sheet_name='Frequent Itemsets', index=False)

    print(f"\n[SUCCESS] Data disimpan ke: {output_file}")
    print("Buka file Excel tersebut untuk copy ke tabel skripsi!\n")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()