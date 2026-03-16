import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_youtube(video_id):

    url = f"https://www.youtube.com/watch?v={video_id}"

    # ---------- Extract page metadata ----------
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("meta", property="og:title")
    title = title_tag["content"] if title_tag else "Unknown"

    # Channel name (author)
    author_tag = soup.find("link", itemprop="name")
    author = author_tag["content"] if author_tag else "Unknown"

    # Description
    description_tag = soup.find("meta", {"name": "description"})
    description = description_tag["content"] if description_tag else ""

    published_date = "Unknown"  # YouTube page does not easily expose it without API

    # ---------- Transcript extraction ----------
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        content_chunks = [t.text.strip() for t in transcript if t.text.strip()]

    except Exception:
        content_chunks = ["Transcript not available"]

    # Combine text for tagging
    full_text = description + " " + " ".join(content_chunks)

    # ---------- Topic extraction ----------
    topics = extract_topics(full_text)

    # ---------- Trust score ----------
    trust_score = calculate_trust_score("youtube", author, content_chunks)

    return {
        "source_url": url,
        "source_type": "youtube",
        "title": title,
        "author": author,
        "published_date": published_date,
        "language": "en",
        "region": "global",
        "topic_tags": topics,
        "trust_score": trust_score,
        "content_chunks": content_chunks[:20]
    }


if __name__ == "__main__":

    video_id = "kJQP7kiw5Fk"

    data = scrape_youtube(video_id)

    print(data)
