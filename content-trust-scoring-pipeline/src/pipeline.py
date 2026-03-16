import json
import os

from blog_scraper import scrape_blog
from youtube_scraper import scrape_youtube
from pubmed_scraper import scrape_pubmed


# ---------- Source Lists ----------

blog_urls = [
    "https://www.healthline.com/nutrition/gut-microbiome-and-health",
    "https://www.healthline.com/nutrition/11-super-healthy-probiotic-foods",
    "https://www.healthline.com/nutrition/8-health-benefits-of-probiotics"
]

youtube_videos = [
    "JaXMGFShqDE",
    "AsyzqhFKLoI"
]

pubmed_ids = [
    "33136284",
    "35105664"
]


# ---------- Dataset Container ----------

dataset = []


# ---------- Blog Scraping ----------
for url in blog_urls:
    try:
        print(f"Scraping blog: {url}")
        dataset.append(scrape_blog(url))
    except Exception as e:
        print(f"Failed blog scrape: {url} | {e}")


# ---------- YouTube Scraping ----------
for vid in youtube_videos:
    try:
        print(f"Scraping YouTube: {vid}")
        dataset.append(scrape_youtube(vid))
    except Exception as e:
        print(f"Failed YouTube scrape: {vid} | {e}")


# ---------- PubMed Scraping ----------
for pmid in pubmed_ids:
    try:
        print(f"Scraping PubMed: {pmid}")
        dataset.append(scrape_pubmed(pmid))
    except Exception as e:
        print(f"Failed PubMed scrape: {pmid} | {e}")


# ---------- Save Dataset ----------

os.makedirs("data", exist_ok=True)

with open("data/dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4, ensure_ascii=False)


print("Dataset generated successfully.")
print(f"Total records collected: {len(dataset)}")
