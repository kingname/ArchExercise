import random
import datetime
from faker import Faker
from jinja2 import Environment, PackageLoader


class HtmlGenerator:
    def __init__(self):
        self.faker = Faker()
        env = Environment(loader=PackageLoader('DataGenerator', 'templates'))
        self.news_template = env.get_template('news.html')
        self.content_template = env.get_template('content.html')

    def generate_news_list(self, page, size, keyword, delay=False):
        news_list = []
        seconds = page * (1 + random.random())
        for _ in range(size):
            if delay:
                seconds += random.randint(60, 600)
            publish_ts = (datetime.datetime.now() - datetime.timedelta(seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S')
            news = {
                'author': self.faker.name(),
                'title': self.faker.paragraph(nb_sentences=1),
                'sample': self.faker.paragraph(nb_sentences=5),
                'url': self.faker.image_url(),
                'publish_ts': publish_ts
            }
            if keyword:
                sample = news['sample']
                insert_index = random.randint(0, len(sample))
                sample = f'{sample[:insert_index]} {keyword} {sample[insert_index:]}'
                news['sample'] = sample
            news_list.append(news)
        news_list.sort(key=lambda x: x['publish_ts'], reverse=True)
        return news_list

    def generate(self, page, size, keyword, delay=False):
        html = self.news_template.render(
            news_list=self.generate_news_list(page, size, keyword, delay),
        )
        return html

    def generate_content(self, page, size, keyword):
        html = self.content_template.render(
            news_list=self.generate_news_list(page, size, keyword),
        )
        return html
