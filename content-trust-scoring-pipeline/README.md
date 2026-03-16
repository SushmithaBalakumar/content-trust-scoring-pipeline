# Content Trust Scoring Pipeline

## Overview

This project implements a **multi-source content ingestion and reliability scoring pipeline** designed for AI-driven applications that require trustworthy knowledge sources.

The system collects information from heterogeneous sources and converts it into a **structured dataset enriched with metadata, topic tags, content chunks, and reliability scores**.

The goal of this project is to demonstrate how different types of knowledge sources can be **normalized, analyzed, and ranked based on credibility** before being used in AI systems such as:

* Retrieval-Augmented Generation (RAG)
* AI knowledge assistants
* Health information systems
* Content recommendation engines

By combining multiple sources and assigning reliability scores, the pipeline helps downstream AI models **prioritize high-quality information**.

---

# Project Structure

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

---

# Module Description

### blog_scraper.py

Scrapes blog articles and extracts:

* Title
* Author
* Publication date
* Article content

The content is cleaned and split into **content chunks** suitable for AI processing.

---

### youtube_scraper.py

Fetches transcripts from YouTube videos using the YouTube Transcript API.

The transcript is converted into structured text chunks that can be used in AI pipelines.

---

### pubmed_scraper.py

Retrieves biomedical research abstracts from **PubMed** using the NCBI API.

Scientific articles are included to introduce **high-credibility sources** into the dataset.

---

### tagging.py

Performs simple NLP-based topic extraction.

It identifies the **most frequent meaningful words** in the text and assigns them as topic tags.

Example:

```
["microbiome", "health", "bacteria", "microbes", "brain"]
```

These tags help enable **semantic search and filtering** in downstream AI systems.

---

### scoring.py

Computes a **trust score** for each source based on multiple credibility signals.

---

### pipeline.py

The main orchestrator of the system.

It performs:

1. Source ingestion
2. Metadata extraction
3. Topic tagging
4. Trust score computation
5. Dataset generation

The final dataset is **sorted by trust_score so that higher reliability sources appear first**.

---

# Data Sources

The pipeline ingests information from three different content types.

### Blogs

Health and nutrition articles from credible websites.

### YouTube

Educational videos with transcripts explaining scientific concepts.

### PubMed

Peer-reviewed biomedical research papers.

---

### Dataset Composition

For this assignment the dataset contains:

* **3 Blog Articles**
* **2 YouTube Videos**
* **2 PubMed Research Papers**

---

# Pipeline Architecture

The pipeline follows a modular ingestion workflow.

### 1 Content Scraping

Content is collected from blog pages, YouTube transcripts, and PubMed abstracts.

---

### 2 Metadata Extraction

Key metadata fields are extracted:

* Title
* Author
* Publication date
* Language
* Region

---

### 3 Content Processing

The text is cleaned and segmented into **content chunks**.

Chunking helps prepare the data for **LLM-based retrieval systems**.

---

### 4 Topic Tagging

Frequent keywords are extracted to generate topic tags.

These tags allow the system to categorize and search information more effectively.

---

### 5 Trust Scoring

Each source is assigned a **trust score** using multiple credibility signals.

The score is computed using:

```
trust_score =
source_weight +
author_presence +
content_length +
citation_presence
```

### Source Weight

| Source Type | Base Score |
| ----------- | ---------- |
| PubMed      | 0.50       |
| Blog        | 0.25       |
| YouTube     | 0.20       |

### Additional Signals

| Signal            | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| Author Presence   | Sources with identified authors receive additional credibility |
| Content Length    | Longer informative content increases reliability               |
| Citation Keywords | Research-related keywords increase credibility                 |

The final trust score ranges between **0 and 1**.

---

# Dataset Ranking

After computing trust scores, the dataset is **sorted by reliability**.

Example ranking:

```
1. PubMed Research Paper     — 0.85
2. PubMed Research Paper     — 0.85
3. Blog Article              — 0.70
4. Blog Article              — 0.70
5. Blog Article              — 0.60
6. YouTube Educational Video — 0.50
7. YouTube Educational Video — 0.50
```

This ranking helps AI systems **prioritize trustworthy sources during retrieval**.

---

# Output

The final structured dataset is stored in:

```
data/dataset.json
```

Each record contains the following fields:

```
source_url
source_type
title
author
published_date
language
region
topic_tags
trust_score
content_chunks
```

This structure allows easy integration with:

* AI search systems
* recommendation engines
* knowledge graphs
* Retrieval-Augmented Generation (RAG) pipelines

---

# How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run the ingestion pipeline:

```
python src/pipeline.py
```

The pipeline will:

1. Scrape all configured sources
2. Extract metadata
3. Generate topic tags
4. Compute trust scores
5. Rank sources by reliability
6. Produce the final dataset

---

## Knowledge Retrieval
The project also includes a simple query system that allows users to retrieve trusted information from the dataset.

Example:
'''
python src/query.py microbiome
'''

The system searches the dataset and returns the most relevant sources ranked by trust_score.
This demonstrates how the dataset could be used in Retrieval-Augmented Generation (RAG) pipelines where AI systems prioritize high-credibility information.

# Notes

This project demonstrates how real-world AI systems prepare knowledge before using it in machine learning models.

In production AI pipelines, raw web data must first be:

* normalized
* enriched with metadata
* ranked for reliability
* structured for retrieval

This pipeline simulates the **knowledge ingestion layer of an AI system**, where heterogeneous sources are transformed into structured, ranked datasets suitable for downstream AI applications.
