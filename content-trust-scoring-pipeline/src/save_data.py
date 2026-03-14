import json
from blog_scraper import scrape_blog

url = "https://www.healthline.com/nutrition/probiotics-101"

data = scrape_blog(url)

with open("data/scraped_data.json", "w") as f:
    json.dump([data], f, indent=4)