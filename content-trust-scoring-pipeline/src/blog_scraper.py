import requests
from bs4 import BeautifulSoup
from langdetect import detect
import json

from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_blog(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # ---------- Title ----------
    title_tag = soup.find("meta", property="og:title")
    if title_tag:
        title = title_tag.get("content", "Unknown")
    else:
        title = soup.find("title").text if soup.find("title") else "Unknown"

    # ---------- Author ----------
    author = "Unknown"

    author_tag = soup.find("meta", {"name": "author"})
    if author_tag:
        author = author_tag.get("content", "Unknown")

    # ---------- Published Date ----------
    published_date = "Unknown"

    date_tag = soup.find("meta", {"property": "article:published_time"})
    if date_tag:
        published_date = date_tag.get("content", "Unknown")

    # ---------- JSON-LD Fallback (Healthline fix) ----------
    if author == "Unknown" or published_date == "Unknown":

        json_scripts = soup.find_all("script", type="application/ld+json")

        for script in json_scripts:
            try:
                data = json.loads(script.string)

                if isinstance(data, list):
                    data = data[0]

                # Extract author
                if author == "Unknown" and "author" in data:
                    if isinstance(data["author"], dict):
                        author = data["author"].get("name", "Unknown")

                    elif isinstance(data["author"], list):
                        author = data["author"][0].get("name", "Unknown")

                # Extract published date
                if published_date == "Unknown" and "datePublished" in data:
                    published_date = data.get("datePublished", "Unknown")

            except:
                continue

    # ---------- Extract Paragraphs ----------
    paragraphs = soup.find_all("p")

    cleaned_paragraphs = []

    for p in paragraphs:

        text = p.get_text().strip()

        if (
            len(text) > 80
            and "Bezzy" not in text
            and "advertisement" not in text.lower()
        ):
            cleaned_paragraphs.append(text)

    content = " ".join(cleaned_paragraphs)

    # ---------- Language Detection ----------
    try:
        language = detect(content)
    except:
        language = "unknown"

    # ---------- Topic Extraction ----------
    topics = extract_topics(content)

    # ---------- Content Chunks ----------
    content_chunks = cleaned_paragraphs[:10]

    # ---------- Trust Score ----------
    trust_score = calculate_trust_score(
        "blog",
        author,
        content_chunks,
        published_date
    )

    return {
        "source_url": url,
        "source_type": "blog",
        "title": title,
        "author": author,
        "published_date": published_date,
        "language": language,
        "region": "unknown",
        "topic_tags": topics,
        "trust_score": trust_score,
        "content_chunks": content_chunks
    }


if __name__ == "__main__":

    test_url = "https://www.healthline.com/nutrition/probiotics-101"

    data = scrape_blog(test_url)

    print(data)
