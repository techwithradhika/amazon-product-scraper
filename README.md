# Amazon Product Scraping

This repository contains Python scripts to scrape Amazon product details. The first script scrapes product links from a given category page, while the second script extracts details (such as product name, rating, price, and seller) from each individual product page.

## Requirements

- Python 3.x
- `requests`: A simple HTTP library for Python.
- `beautifulsoup4`: A library for web scraping purposes to extract data from HTML and XML documents.
- `csv`: Python's built-in CSV library for reading and writing CSV files.

### Installation

**Clone the repository:**

```bash
git clone https://github.com/techwithradhika/amazon-product-scraper.git
```

Navigate to the project directory:
```bash
cd amazon-product-scraper
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
Activate the virtual environment:
```bash
.\venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install requests beautifulsoup4
```

Usage
**Scrape product links from a category page:**
Run the following script to scrape product links from a given Amazon category page (e.g., a list of products in a category):
```bash
python scrape_product_links.py
```
This will generate a CSV file named amazon_product_links.csv containing all the product links.

Extract product details from the links:
After scraping the product links, run the second script to extract the details for each product:

```bash
python scrape_product_details.py
```
This will process each link in amazon_product_links.csv, extract the product name, rating, price, and seller name, and save the details in amazon_product_details.csv.
