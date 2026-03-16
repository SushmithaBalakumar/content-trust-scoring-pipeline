import json
import sys

def search_dataset(keyword):

    with open("data/dataset.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    results = []

    for item in dataset:

        text = " ".join(item["content_chunks"]).lower()

        if keyword.lower() in text or keyword.lower() in item["topic_tags"]:
            results.append(item)

    results_sorted = sorted(results, key=lambda x: x["trust_score"], reverse=True)

    return results_sorted


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python query.py <keyword>")
        sys.exit()

    keyword = sys.argv[1]

    results = search_dataset(keyword)

    print(f"\nTop trusted sources for topic: {keyword}\n")

    for i, r in enumerate(results[:5], 1):

        print(f"{i}. {r['source_type'].upper()} ({r['trust_score']})")
        print(r["title"])
        print(r["source_url"])
        print()
