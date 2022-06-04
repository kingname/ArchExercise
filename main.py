import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from DataGenerator import JsonGenerator, HtmlGenerator


app = FastAPI()
json_generator = JsonGenerator()
html_genrator = HtmlGenerator()


@app.get('/')
def index():
    return {'success': True,
            'title': '大数据爬虫架构进阶课程配套练习网站。',
            'author': '青南',
            'mail': 'contact@kingname.info',
            'wechat_official_account': '未闻Code',
            'doc': '/redoc'}


@app.get('/html/news')
def news(page: int = 0, size: int = 10, keyword: str = '', delay: bool = False):
    """
    获取自动生成的新闻HTML页面

    :param page: 任意数字

    :param size: 任意小于50的数字

    :param keyword: 关键字

    :param delay: 新闻发布时间是否添加随机延迟
    """
    html = html_genrator.generate(page, size, keyword, delay)
    return HTMLResponse(html)


@app.get('/api')
def profile(page: int = 0, size: int = 10, data_type: str = 'outer_json', keyword: str = ''):
    """
    模拟API Ajax请求的返回

    :param page: 任意数字

    :param size: 任意数字

    :param data_type: inner_json/outer_json/html

    :param keyword: 关键字
    """
    if data_type == 'html':
        data = html_genrator.generate_content(page, size, keyword)
    else:
        data = json_generator.generate(size)
        if data_type == 'outer_json':
            data = json.loads(data)
    result = {
        'success': True,
        'total': 999999999999,
        'page': page,
        'data': data
    }
    return result
