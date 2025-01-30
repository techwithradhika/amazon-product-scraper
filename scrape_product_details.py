import requests
from bs4 import BeautifulSoup
import csv

def extract_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    try:
        response = requests.get(url, headers=headers, verify=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            product_name = soup.find("span", {"id": "productTitle"})
            if product_name:
                product_name = product_name.get_text(strip=True)
            else:
                product_name = "N/A"
            
            rating = soup.find("span", {"id": "acrPopover"})
            if rating:
                rating = rating.get_text(strip=True)  
            else:
                rating = "N/A"
            
            price = soup.find("span", {"class": "a-price-whole"})
            if price:
                price = price.get_text(strip=True)
            else:
                price = "N/A"
            
            seller_name = soup.find("a", {"id": "sellerProfileTriggerId"})
            if seller_name:
                seller_name = seller_name.get_text(strip=True)
            else:
                seller_name = "N/A"
            
            return [product_name, rating, price, seller_name]
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return ["Error", "Error", "Error", "Error"]
    
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ["Error", "Error", "Error", "Error"]

with open('amazon_product_links.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    links = [row[0] for row in reader][1:]  

with open('amazon_product_details.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Rating", "Price", "Seller Name"])
    
    for link in links:
        print(f"Processing {link}...")
        product_details = extract_product_details(link)
        writer.writerow(product_details)
    
    print("Product details saved to amazon_product_details.csv")
