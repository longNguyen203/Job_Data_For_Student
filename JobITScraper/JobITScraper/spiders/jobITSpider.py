from scrapy.selector import SelectorList
from JobITScraper.items import JobitscraperItem
from fake_useragent import UserAgent
from urllib.parse import urlencode
import scrapy 


API_KEY = '4db8ec44-b4ad-4257-b408-c1d1b2cb7d0e'

def get_proxy_url(url) -> str:
    payload = { 'api_key': API_KEY, 'url': url }
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class JobITSpider(scrapy.Spider):

    name = 'JobITCrawling'

    allowed_domains: list = ['topcv.vn', 'proxy.scrapeops.io']
    start_urls: list = ['https://www.topcv.vn/viec-lam-it']
    page_num: int = 1

    usr_agnt = UserAgent(browsers=[
            'chrome', 'google', 'edge', 'firefox', 'safari', 'internetexplorer', 'opera', 'android', 'ios'
    ])
    user_agent: str = usr_agnt.random
    
    custom_settings = {
        'FEEDS': { 'result.json': {'format': 'json', 'overwrite': True} },
        'DOWNLOAD_DELAY': 1 
    }

    def start_requests(self) -> None:
        yield scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse, headers={'User-Agent': self.user_agent})
    
    def parse(self, response) -> None:

        jobs: SelectorList = response.css('div.job-list-2 div.job-item-2')
        PAGES_NUMBER = 38

        for job in jobs:
            relative_url = job.css('div.avatar a::attr(href)').get()
            if relative_url is not None:
                yield scrapy.Request(url=get_proxy_url(relative_url), callback=self.parse_job_page, headers={'User-Agent': self.user_agent})

        next_page = 'https://www.topcv.vn/viec-lam-it?page={}'.format(JobITSpider.page_num)

        if next_page is not None and JobITSpider.page_num <= PAGES_NUMBER:
            JobITSpider.page_num += 1
            yield scrapy.Request(url=get_proxy_url(next_page), callback=self.parse, headers={'User-Agent': self.user_agent})
        
    def parse_job_page(self, response) -> None:

        table_info = response.css('div.box-general-content div.box-general-group-info')
        description = response.css('div.job-description__item--content')
        jobitscraperItem = JobitscraperItem()

        print('***User_Agent***:', JobITSpider.user_agent)
        JobITSpider.user_agent = JobITSpider.usr_agnt.random

        try:
            jobitscraperItem['title'] = response.css('h1.job-detail__info--title ::text').getall()
            jobitscraperItem['name'] = response.css('h1.job-detail__info--title a::text').get()
            jobitscraperItem['salary'] = response.css('div.job-detail__info--section-content-value::text').get()
            jobitscraperItem['address'] = response.css('div.job-description__item--content div ::text').getall()
            jobitscraperItem['time'] = response.css('div.job-detail__info--deadline::text').getall()
            jobitscraperItem['rank'] = table_info[0].css('div.box-general-group-info-value ::text').get()
            jobitscraperItem['experience'] = table_info[1].css('div.box-general-group-info-value ::text').get()
            jobitscraperItem['number_of_recruits'] = table_info[2].css('div.box-general-group-info-value ::text').get()
            jobitscraperItem['working_form'] = table_info[3].css('div.box-general-group-info-value ::text').get()
            jobitscraperItem['sex'] = table_info[4].css('div.box-general-group-info-value ::text').get()
            jobitscraperItem['company'] = response.css('h2.company-name-label a ::text').get()
            jobitscraperItem['description'] = description[0].css('div.job-description__item--content li ::text').getall()
            jobitscraperItem['requirements'] = description[1].css('div.job-description__item--content li ::text').getall()
            jobitscraperItem['benefit'] = description[2].css('div.job-description__item--content p ::text').getall()
            jobitscraperItem['url'] = response.url
        except IndexError:
            print("Loi chi muc !!!!")

        yield jobitscraperItem

