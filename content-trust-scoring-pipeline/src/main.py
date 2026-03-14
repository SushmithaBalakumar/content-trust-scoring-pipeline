import json
from blog_scraper import scrape_blog

blog_urls = [
    "https://www.healthline.com/nutrition/probiotics-101",
    "https://www.healthline.com/nutrition/10-super-healthy-probiotic-foods",
    "https://www.healthline.com/nutrition/gut-health-and-probiotics"
]

dataset = []

for url in blog_urls:
    try:
        data = scrape_blog(url)
        dataset.append(data)
        print(f"Scraped: {url}")
    except Exception as e:
        print(f"Failed: {url}")

with open("data/dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)