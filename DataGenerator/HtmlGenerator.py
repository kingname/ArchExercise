import random
from faker import Faker
from jinja2 import Environment, PackageLoader


class HtmlGenerator:
    def __init__(self):
        self.faker = Faker()
        env = Environment(loader=PackageLoader('DataGenerator', 'templates'))
        self.news_template = env.get_template('news.html')
        self.content_template = env.get_template('content.html')

    def generate_news_list(self, size, keyword):
        news_list = []
        for _ in range(size):
            news = {
                'author': self.faker.name(),
                'title': self.faker.paragraph(nb_sentences=1),
                'sample': self.faker.paragraph(nb_sentences=5),
                'url': self.faker.image_url(),
                'publish_ts': self.faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            }
            if keyword:
                sample = news['sample']
                insert_index = random.randint(0, len(sample))
                sample = f'{sample[:insert_index]} {keyword} {sample[insert_index:]}'
                news['sample'] = sample
            news_list.append(news)
        return news_list

    def generate(self, page, size, keyword):
        html = self.news_template.render(
            news_list=self.generate_news_list(size, keyword),
        )
        return html

    def generate_content(self, size, keyword):
        html = self.content_template.render(
            news_list=self.generate_news_list(size, keyword),
        )
        return html
