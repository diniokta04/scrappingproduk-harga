import requests
from bs4 import BeautifulSoup
import json
import os

DATA_FILE = "data.json"

def scrape_ke_json():
    url = "https://web-scraping.dev/product/1"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    print(f"\nSedang mengambil data dari {url}...")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
        
            title = soup.find("h3", class_="product-title").get_text(strip=True)
            price_raw = soup.find("span", class_="product-price").get_text(strip=True)
            
            price = price_raw.replace('$', '').replace(',', '')
            
            data = load_data()
            new_id = max([item["id"] for item in data], default=0) + 1
            
            data.append({
                "id": new_id,
                "nama": title,
                "harga": price
            })
            
            save_data(data)
            print(f"Berhasil scrape: {title} (ID: {new_id})")
        else:
            print("Gagal scrape: Status code", response.status_code)
    except Exception as e:
        print(f"Error saat scraping: {e}")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def tambah_item(nama, harga):
    data = load_data()
    new_id = max([item["id"] for item in data], default=0) + 1
    data.append({"id": new_id, "nama": nama, "harga": harga})
    save_data(data)
    print(f"Item '{nama}' berhasil ditambahkan manual.")

def lihat_semua():
    data = load_data()
    print("\n--- DAFTAR DATA ---")
    if not data:
        print("Data kosong.")
    for item in data:
        print(f"ID: {item['id']} | {item['nama']} - Harga: {item['harga']}")

def update_item(item_id, nama_baru, harga_baru):
    data = load_data()
    for item in data:
        if item["id"] == item_id:
            item["nama"] = nama_baru
            item["harga"] = harga_baru
            save_data(data)
            print(f"ID {item_id} berhasil diperbarui.")
            return
    print("ID tidak ditemukan.")

def hapus_item(item_id):
    data = load_data()
    new_data = [item for item in data if item["id"] != item_id]
    save_data(new_data)
    print(f"ID {item_id} berhasil dihapus.")

def menu():
    while True:
        print("\n" + "="*20)
        print("  SISTEM SCRAPE & CRUD")
        print("="*20)
        print("1. Jalankan Scrape (Ambil dari Web)")
        print("2. Tambah Manual")
        print("3. Lihat Semua Data")
        print("4. Update Item")
        print("5. Hapus Item")
        print("6. Keluar")
        
        pilih = input("Pilih menu (1-6): ")
        
        if pilih == "1":
            scrape_ke_json()
        elif pilih == "2":
            nama = input("Nama: ")
            harga = input("Harga: ")
            tambah_item(nama, harga)
        elif pilih == "3":
            lihat_semua()
        elif pilih == "4":
            item_id = int(input("ID item yang diupdate: "))
            nama = input("Nama baru: ")
            harga = input("Harga baru: ")
            update_item(item_id, nama, harga)
        elif pilih == "5":
            item_id = int(input("ID item yang dihapus: "))
            hapus_item(item_id)
        elif pilih == "6":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()