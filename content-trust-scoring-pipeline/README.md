# Content Trust Scoring Pipeline

## Overview

This project implements a **multi-source content ingestion and reliability scoring pipeline** designed for AI-driven applications that require trustworthy knowledge sources.

The system collects content from multiple domains and transforms it into a **structured dataset enriched with metadata, topic tags, and reliability scores**.

The goal is to demonstrate how heterogeneous data sources can be normalized and evaluated for **AI knowledge pipelines such as retrieval systems, health assistants, or recommendation systems**.

## Project Structure

```
content-trust-scoring-pipeline
│
├── src
│   ├── blog_scraper.py
│   ├── youtube_scraper.py
│   ├── pubmed_scraper.py
│   ├── tagging.py
│   ├── scoring.py
│   └── pipeline.py
│
├── data
│   └── dataset.json
│
├── requirements.txt
└── README.md
```

### Description

* **blog_scraper.py** – Extracts content and metadata from blog articles
* **youtube_scraper.py** – Retrieves YouTube transcripts and processes text
* **pubmed_scraper.py** – Collects biomedical abstracts from PubMed
* **tagging.py** – Generates topic tags using keyword frequency
* **scoring.py** – Computes source reliability scores
* **pipeline.py** – Orchestrates the full ingestion and dataset generation process

## Data Sources

The pipeline ingests information from three different content types:

* **Blogs** – Health and nutrition articles
* **YouTube** – Educational videos with transcripts
* **PubMed** – Peer-reviewed biomedical research articles

For this assignment the dataset includes:

* 3 Blog Articles
* 2 YouTube Videos
* 2 PubMed Research Papers

## Pipeline Architecture

The system follows a modular ingestion workflow:

### 1. Content Scraping

Collect text content from blog pages, YouTube transcripts, and PubMed abstracts.

### 2. Metadata Extraction

Extract source information such as title, author, publication date, and language.

### 3. Content Processing

Clean and segment text into smaller **content chunks** suitable for downstream AI processing.

### 4. Topic Tagging

Extract frequently occurring keywords to identify dominant topics within the content.

### 5. Trust Scoring

Assign a reliability score based on the **type of source** and available metadata.

### 6. Dataset Generation

Consolidate all processed entries into a unified JSON dataset.

## Trust Scoring Logic

Each content source is assigned a baseline reliability score based on its credibility.

| Source Type | Trust Score | Reason                             |
| ----------- | ----------- | ---------------------------------- |
| PubMed      | 0.5         | Peer-reviewed scientific research  |
| Blog        | 0.3         | Informational but not academic     |
| YouTube     | 0.2         | User-generated educational content |

This simple scoring framework demonstrates how **source reliability can be incorporated into AI knowledge pipelines**.

---

## Output

The final structured dataset is stored in:

```
data/dataset.json
```

Each record contains:

* source_url
* source_type
* title
* author
* published_date
* language
* region
* topic_tags
* trust_score
* content_chunks

This structure enables easy integration with **search systems, recommendation engines, or Retrieval-Augmented Generation (RAG) pipelines**.

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the ingestion pipeline:

```
python src/pipeline.py
```

The pipeline will scrape all sources, process the content, and generate the final dataset automatically.


## Notes

This pipeline design mirrors real-world **AI ingestion systems**, where heterogeneous knowledge sources are normalized, enriched with metadata, and scored for reliability before being used in downstream retrieval or decision-support models.
