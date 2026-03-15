import requests
from bs4 import BeautifulSoup
from langdetect import detect
from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_blog(url):

    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title = soup.find("title").text if soup.find("title") else ""

    # Author
    author_tag = soup.find("meta", {"name": "author"})
    author = author_tag["content"] if author_tag else "Unknown"

    # Published date
    date_tag = soup.find("meta", {"property": "article:published_time"})
    published_date = date_tag["content"] if date_tag else "Unknown"

    # Extract paragraphs
    paragraphs = soup.find_all("p")
    content = " ".join([p.get_text() for p in paragraphs])
    topics = extract_topics(content)

    # Language detection
    try:
        language = detect(content)
    except:
        language = "unknown"

    # Chunk content
    content_chunks = [
        p.get_text().strip()
        for p in paragraphs
        if len(p.get_text().strip()) > 80
        and "Bezzy" not in p.get_text()
    ]
    trust_score = calculate_trust_score("blog", author, content_chunks)



    return {
        "source_url": url,
        "source_type": "blog",
        "title": title,
        "published_date": published_date,
        "language": language,
        "region": "unknown",
        "topic_tags": topics,
        "author": author,
        "trust_score": trust_score,
        "content_chunks": content_chunks[:10]
    }


if __name__ == "__main__":

    test_url = "https://www.healthline.com/nutrition/probiotics-101"

    data = scrape_blog(test_url)

    print(data)
