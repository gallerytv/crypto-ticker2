import feedparser
from datetime import datetime
from pathlib import Path

# Список RSS-источников
feeds = [
    'https://www.coindesk.com/arc/outboundfeeds/rss/',
    'https://cointelegraph.com/rss',
    'https://cryptoslate.com/feed/',
    'https://decrypt.co/feed',
    'https://www.binance.com/en/news/rss'
]

def get_headlines():
    headlines = []
    for url in feeds:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:2]:
                headlines.append(entry.title.upper())
        except Exception as e:
            continue
    return headlines

def update_html(headlines):
    html_text = ' • '.join(headlines)
    template = Path('index.html').read_text(encoding='utf-8')
    start = template.find('<div class="ticker-text">') + len('<div class="ticker-text">')
    end = template.find('</div>', start)
    new_html = template[:start] + '\n      ' + html_text + '\n    ' + template[end:]
    Path('index.html').write_text(new_html, encoding='utf-8')

if __name__ == '__main__':
    headlines = get_headlines()
    update_html(headlines)
