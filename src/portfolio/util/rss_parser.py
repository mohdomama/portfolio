import feedparser

FEED_URL = "https://medium.com/feed/@mohdomama"


def get_feed():
    entries = []
    feed = feedparser.parse(FEED_URL)
    for entry in feed.entries:
        # There should be a better way to filter out blog responses
        if len(entry.content[0].value) > 1000:
            entries.append(entry)

    return entries


def main():
    entries = get_feed()
    for entry in entries:
        print(entry.title)
        print(entry.published)
        print(entry.link)

        print("*******")
    print(entry.keys())


if __name__ == '__main__':
    main()
