import json

from blog_scraper import scrape_blog
from youtube_scraper import scrape_youtube
from pubmed_scraper import scrape_pubmed


blog_urls = [
"https://www.healthline.com/nutrition/probiotics-101",
"https://www.healthline.com/nutrition/11-super-healthy-probiotic-foods",
"https://www.healthline.com/nutrition/8-health-benefits-of-probiotics"
]

youtube_videos = [
    "JaXMGFShqDE",
    "AsyzqhFKLoI"
]

pubmed_ids = [
"35105664",
"33136284"
]


dataset = []

for url in blog_urls:
    dataset.append(scrape_blog(url))

for vid in youtube_videos:
    dataset.append(scrape_youtube(vid))

for pmid in pubmed_ids:
    dataset.append(scrape_pubmed(pmid))


with open("data/dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Dataset generated successfully.")