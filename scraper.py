import feedparser
import csv

def scrape_legislation_feed(feed_url):
    feed = feedparser.parse(feed_url)
    results = []

    for entry in feed.entries:
        title = entry.title.strip()
        url = entry.link
        results.append((title, url))

    return results

if __name__ == "__main__":
    all_items = []

    for page in range(1, 102):  # Pages 1 to 101 inclusive
        url = f"https://www.legislation.gov.uk/primary+secondary/2025/data.feed?page={page}"
        items = scrape_legislation_feed(url)
        all_items.extend(items)

    # Write to CSV
    with open("uk_legislations_2025_all.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Link"])  # Header
        writer.writerows(all_items)

    print("Saved to uk_legislations_2025_all.csv")
