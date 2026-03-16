import requests
import xml.etree.ElementTree as ET

from scoring import calculate_trust_score
from tagging import extract_topics


def scrape_pubmed(pmid):

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"

    response = requests.get(url)

    root = ET.fromstring(response.content)

    # ---------- Title ----------
    title = root.find(".//ArticleTitle")
    title_text = title.text if title is not None else "Unknown"

    # ---------- Abstract ----------
    abstract = root.find(".//AbstractText")
    abstract_text = abstract.text if abstract is not None else "No abstract available"

    # ---------- Authors ----------
    authors = root.findall(".//Author")
    author_names = []

    for author in authors:
        last = author.find("LastName")
        first = author.find("ForeName")

        if last is not None and first is not None:
            author_names.append(f"{first.text} {last.text}")

    author = ", ".join(author_names[:3]) if author_names else "Unknown"

    # ---------- Journal ----------
    journal = root.find(".//Journal/Title")
    journal_name = journal.text if journal is not None else "Unknown"

    # ---------- Publication Year ----------
    year = root.find(".//PubDate/Year")
    published_date = year.text if year is not None else "Unknown"

    # ---------- Chunk abstract ----------
    content_chunks = [c.strip() for c in abstract_text.split(". ") if c.strip()]

    # ---------- Topic tagging ----------
    topics = extract_topics(abstract_text)

    # ---------- Trust score ----------
    trust_score = calculate_trust_score("pubmed", author, content_chunks, published_date)

    return {
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "source_type": "pubmed",
        "title": title_text,
        "author": author,
        "journal": journal_name,
        "published_date": published_date,
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
