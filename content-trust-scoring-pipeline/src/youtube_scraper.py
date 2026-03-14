from youtube_transcript_api import YouTubeTranscriptApi
from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_youtube(video_id):

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        content_chunks = [t.text for t in transcript]
        full_text = " ".join(content_chunks)

    except Exception:
        content_chunks = ["Transcript not available"]
        full_text = ""

    # Topic extraction
    topics = extract_topics(full_text)

    # Trust scoring
    trust_score = calculate_trust_score("youtube", "Unknown", "Unknown")

    return {
        "source_url": f"https://www.youtube.com/watch?v={video_id}",
        "source_type": "youtube",
        "author": "Unknown",
        "published_date": "Unknown",
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