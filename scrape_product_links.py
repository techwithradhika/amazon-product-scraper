import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

try:
    response = requests.get(url, headers=headers, verify=True)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        product_links = []
        for item in soup.find_all("a", {"class": "a-link-normal s-line-clamp-4 s-link-style a-text-normal"}):
            link = "https://www.amazon.in" + item.get("href")
            product_links.append(link)

        with open('amazon_product_links.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Links"]) 
            for link in product_links:
                writer.writerow([link]) 
        print("Product links saved to amazon_product_links.csv")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
except Exception as e:
    print(f"Error scraping {url}: {e}")
