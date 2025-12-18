from fpdf import FPDF

def input_barang():
    data = []
    print("Masukkan data barang. Ketik 'selesai' atau kosongkan nama untuk berhenti.")
    while True:
        nama = input("Nama barang: ")
        if not nama or nama == "selesai":   # nilai sentinel
            break
        try:
            stok = int(input("Stok: "))
            harga = int(input("Harga satuan (Rp): "))
        except ValueError:
            print("Input tidak valid. Ulangi item ini.")
            continue
        data.append({"nama": nama, "stok": stok, "harga": harga})
    return data

def statistik(data):
    jml_item = len(data)
    total_stok = sum(d["stok"] for d in data)
    total_nilai = sum(d["stok"] * d["harga"] for d in data)
    return jml_item, total_stok, total_nilai

def export_pdf(data, ringkas, filename="laporan_inventory.pdf"):
    jml_item, total_stok, total_nilai = ringkas
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Laporan Inventory", ln=1, align="C")

    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 8, f"Jumlah item: {jml_item}", ln=1)
    pdf.cell(0, 8, f"Total stok : {total_stok}", ln=1)
    pdf.cell(0, 8, f"Total nilai: Rp {total_nilai:,}", ln=1)

    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(90, 8, "Nama", border=1)
    pdf.cell(30, 8, "Stok", border=1, align="R")
    pdf.cell(40, 8, "Harga", border=1, align="R")
    pdf.cell(30, 8, "Subtotal", border=1, ln=1, align="R")

    pdf.set_font("Helvetica", size=11)
    for d in data:
        subtotal = d["stok"] * d["harga"]
        pdf.cell(90, 8, d["nama"], border=1)
        pdf.cell(30, 8, str(d["stok"]), border=1, align="R")
        pdf.cell(40, 8, f"Rp {d['harga']:,}", border=1, align="R")
        pdf.cell(30, 8, f"Rp {subtotal:,}", border=1, ln=1, align="R")

    pdf.output(filename)
    print(f"PDF tersimpan: {filename}")

def menu():
    data = input_barang()
    if not data:
        print("Tidak ada data dimasukkan.")
        return
    ringkas = statistik(data)
    print("\nStatistik:")
    print(f"- Jumlah item: {ringkas[0]}")
    print(f"- Total stok : {ringkas[1]}")
    print(f"- Total nilai: Rp {ringkas[2]:,}")

    pilih = input("\nExport ke PDF? (y/n): ")
    export_pdf(data, ringkas)

if __name__ == "__main__":
    menu()
