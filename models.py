# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transaksi(db.Model):
    __tablename__ = 'transaksi'

    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_invoice        = db.Column(db.String(50), nullable=False)
    kode_produk       = db.Column(db.String(100), nullable=False)
    nama_produk       = db.Column(db.String(255), nullable=False)
    tanggal_transaksi = db.Column(db.Date, nullable=False)
    created_at        = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id'               : self.id,
            'no_invoice'       : self.no_invoice,
            'kode_produk'      : self.kode_produk,
            'nama_produk'      : self.nama_produk,
            'tanggal_transaksi': self.tanggal_transaksi.strftime('%d/%m/%Y')
        }


class UploadLog(db.Model):
    __tablename__ = 'upload_log'

    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_file    = db.Column(db.String(255), nullable=False)
    jumlah_baris = db.Column(db.Integer, nullable=False)
    uploaded_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id'          : self.id,
            'nama_file'   : self.nama_file,
            'jumlah_baris': self.jumlah_baris,
            'uploaded_at' : self.uploaded_at.strftime('%d/%m/%Y %H:%M')
        }