import feedparser


TrendFeed = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=UA')
SourceFeed1 = feedparser.parse('https://www.segodnya.ua/xml/rss')
SourceFeed2 = feedparser.parse('https://www.rbc.ua/static/rss/ukrnet.strong.rus.rss.xml')
# SourceFeed3 = feedparser.parse('https://rss.unian.net/site/news_rus.rss')
SourceFeed4 = feedparser.parse('https://www.pravda.com.ua/rus/rss/')
SourceFeed5 = feedparser.parse('https://focus.ua/modules/rss.php')

Sources = [
    SourceFeed1,
    SourceFeed2,
    # SourceFeed3,
    SourceFeed4,
    SourceFeed5,
]

def get_articles():
    trends = []
    result = []
    names = [
        'Сегодня',
        'РБК-Україна',
        'УНИАН',
        'УКРАИНСКАЯ ПРАВДА',
        'ФОКУС'
    ]

    for i in TrendFeed.entries:
        if i.ht_news_item_source in names:
            trends.append(i.ht_news_item_url)


    for Source in Sources:
        for i in Source.entries:
            if i.link in trends:
                dict_ = {
                    'title': i.title,
                    'link': i.link,
                    'pub_date': i.published
            }
                result.append(dict_)

    return result

