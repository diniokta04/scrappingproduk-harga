import requests
from bs4 import BeautifulSoup
import json
import csv

url = "https://web-scraping.dev/product/1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
     
        title = soup.find("h3", class_="product-title").get_text(strip=True)
        price = soup.find("span", class_="product-price").get_text(strip=True)
        
        data_list = []
        data_list.append({
            "produk": title,
            "harga": price,
        })

        with open('hasil_data.json', 'w', encoding='utf-8') as f_json:
            json.dump(data_list, f_json, indent=4, ensure_ascii=False)
        
        keys = data_list[0].keys()
        with open('hasil_data.csv', 'w', newline='', encoding='utf-8') as f_csv:
            dict_writer = csv.DictWriter(f_csv, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_list)

        print("Scraping Berhasil!")
        print(f"Data: {title} - {price}")
        print("-" * 30)
        print("File 'hasil_data.json' dan 'hasil_data.csv' telah dibuat.")

    else:
        print(f"Gagal akses. Status: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")