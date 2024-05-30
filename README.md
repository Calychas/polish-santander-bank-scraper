# Polish Santander Bank Scraper

Scrape all your expenses with their **categories** and **subcategories**!

## Steps

   1. Install all requirements: `pip install -r requirements.txt`
   2. `python scrap.py` - this should scrape all expenses to [pages](./pages)
   3. Run `parse_pages.ipynb` to get all your expenses with subcategories under [wydatki.csv](./wydatki.csv). Additionally, under [wydatki_kategorie.csv](./wydatki_kategorie.csv) you should have expenses with categories and subcategories.
