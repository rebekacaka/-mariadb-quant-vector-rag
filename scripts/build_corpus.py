# Downloads every article in the title list and saves them as one JSON Lines file.
import json
import time

from quantrag.corpus import load_titles
from quantrag.fetch import fetch_article_text

TITLES_FILE = "data_quant/corpus_titles.txt"
OUT_FILE = "data_quant/pages.jsonl"


def main():
    titles = load_titles(TITLES_FILE)
    with open(OUT_FILE, "w", encoding="utf-8") as out:
        for i, title in enumerate(titles, start=1):
            try:
                text = fetch_article_text(title)
            except Exception as err:
                print("skipped", title, err)
                continue
            record = {"title": title, "text": text}
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(i, "of", len(titles), title, len(text))
            time.sleep(0.2)


if __name__ == "__main__":
    main()