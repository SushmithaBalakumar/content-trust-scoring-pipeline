import requests
import xml.etree.ElementTree as ET

from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_pubmed(pmid):

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"

    response = requests.get(url)

    root = ET.fromstring(response.content)

    title = root.find(".//ArticleTitle")
    abstract = root.find(".//AbstractText")

    title_text = title.text if title is not None else "Unknown"
    abstract_text = abstract.text if abstract is not None else "No abstract available"

    # split abstract into chunks
    content_chunks = abstract_text.split(". ")

    # topic tagging
    topics = extract_topics(abstract_text)
    trust_score = calculate_trust_score("pubmed", "Unknown", content_chunks)


    return {
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "source_type": "pubmed",
        "title": title_text,
        "author": "Unknown",
        "published_date": "Unknown",
        "language": "en",
        "region": "global",
        "topic_tags": topics,
        "trust_score": trust_score,
        "content_chunks": content_chunks[:20]
    }


if __name__ == "__main__":

    pmid = "31452104"

    data = scrape_pubmed(pmid)

    print(data)
