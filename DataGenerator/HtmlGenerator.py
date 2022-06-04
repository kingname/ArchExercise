from jinja2 import Template, Environment, PackageLoader
from faker import Faker


class HtmlGenerator:
    def __init__(self):
        self.faker = Faker()
        env = Environment(loader=PackageLoader('DataGenerator', 'templates'))
        self.news_template = env.get_template('news.html')
        self.content_template = env.get_template('content.html')

    def generate_news_list(self, size):
        news_list = []
        for _ in range(size):
            news = {
                'author': self.faker.name(),
                'title': self.faker.paragraph(nb_sentences=1),
                'sample': self.faker.paragraph(nb_sentences=5),
                'url': self.faker.image_url(),
                'publish_ts': self.faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            }
            news_list.append(news)
        return news_list

    def generate(self, page, size):
        html = self.news_template.render(
            news_list=self.generate_news_list(size),
        )
        return html

    def generate_content(self, size):
        html = self.content_template.render(
            news_list=self.generate_news_list(size),
        )
        return html
