# FP-Growth Market Basket Analysis System

A full-stack web application for analyzing product purchase patterns using the **FP-Growth algorithm**, generating product bundling recommendations based on historical transaction data. Built as a practical implementation of academic research (undergraduate thesis) into a fully functional system.

## 📌 Background

Companies with high transaction volumes often struggle to identify which products are frequently purchased together, even though this information is highly valuable for bundling strategies, product placement, and sales recommendations. This project addresses that problem by applying **association rule mining (FP-Growth)** on transaction data to automatically discover purchase patterns.

## ✨ Key Features

- **Manage Data** — upload transaction data in Excel format, with automatic column structure validation and upload history
- **View Result** — run FP-Growth analysis with adjustable parameters (minimum support & confidence), including date range filtering
- **Product Bundling Recommendations** — analysis results are displayed as product combination recommendations along with *support*, *confidence*, and *lift* metrics

## 🖼️ Application Preview

### Manage Data
Upload and manage transaction data with automatic validation.

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/4915965e-49c3-4f1e-aaca-89be58c3ab90" />

### Analysis Result & Bundling Recommendations
Example analysis result on ±1,094 transactions with parameters set at 5% minimum support and 50% minimum confidence, generating 148 association rules:

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/d6f69f31-1adc-4a0b-9764-5511df7abdb3" />

| Recommendation | Support | Confidence | Lift |
|---|---|---|---|
| Product A + Product B | 24.9% | 100.0% | 1.97 |
| Product C + Product D | 26.4% | 100.0% | 1.97 |
| Product E + F + G | 5.3% | 96.7% | 4.28 |

*A lift value above 1 indicates a positive correlation between products — the higher the value, the stronger the tendency for those products to be purchased together.*

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL (SQLAlchemy ORM)
- **Algorithm**: FP-Growth (association rule mining)
- **Frontend**: HTML, Bootstrap 5
- **Data Processing**: Pandas, OpenPyXL

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/raffyandriawan/market-basket-analysis-fpgrowth.git
cd market-basket-analysis-fpgrowth
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Copy `.env.example` to `.env`, then adjust it to match your local database configuration:
```bash
cp .env.example .env
```

### 4. Set up the database
Create a new MySQL database, then update the database name in the `.env` file accordingly.

### 5. Run the application
```bash
python app.py
```
The application will run at `http://localhost:5000`

## 📊 Dataset Note

The original dataset used during development is internal company transaction data and is **not included** in this repository due to confidentiality. The required data structure (`no_invoice`, `kode_produk`, `nama_produk`, `tanggal_transaksi` columns) can be found via the "Download Template" feature on the Manage Data page.

## 📈 Analysis Insight

The analysis revealed that products from complementary categories (e.g., feed and supplements) showed the highest lift values (>4.0), indicating strong opportunities for cross-category bundling strategies — not just frequently co-purchased products within the same category.

## 👤 Author

**Muhammad Raffy Andriawan**
Informatics Engineering, Sriwijaya University

[LinkedIn](https://www.linkedin.com/in/raffyandriawan) · [GitHub](https://github.com/raffyandriawan)
