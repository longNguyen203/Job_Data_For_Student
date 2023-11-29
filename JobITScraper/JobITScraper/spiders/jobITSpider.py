import scrapy 
from scrapy.selector import SelectorList
from JobITScraper.items import JobitscraperItem
from fake_useragent import UserAgent


class JobITSpider(scrapy.Spider):

    name = 'JobITCrawling'

    allowed_domains: list = ['topcv.vn']
    start_urls: list = ['https://www.topcv.vn/viec-lam-it']
    page_num: int = 1

    usr_agnt = UserAgent(browsers=['chrome', 'google', 'edge', 'firefox', 'safari'])
    user_agent: str = usr_agnt.random

    custom_settings = {
        'FEEDS': { 'result.json': {'format': 'json', 'overwrite': True} }
    }

    def parse(self, response) -> None:

        jobs: SelectorList = response.css('div.job-list-2 div.job-item-2')
        PAGES_NUMBER = 10

        for job in jobs:
            relative_url = job.css('div.avatar a::attr(href)').get()
            if relative_url is not None:
                yield response.follow(relative_url, callback=self.parse_job_page, headers={'User-Agent': self.user_agent})

        next_page = 'https://www.topcv.vn/viec-lam-it?page={}'.format(JobITSpider.page_num)

        if next_page is not None and JobITSpider.page_num <= PAGES_NUMBER:
            JobITSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse, headers={'User-Agent': self.user_agent})
        

    def parse_job_page(self, response) -> None:

        table_info = response.css('div.box-general-content div.box-general-group-info')
        description = response.css('div.job-description__item--content')
        jobitscraperItem = JobitscraperItem()

        jobitscraperItem['title'] = response.css('h1.job-detail__info--title ::text').getall()
        jobitscraperItem['name'] = response.css('h1.job-detail__info--title a::text').get()
        jobitscraperItem['salary'] = response.css('div.job-detail__info--section-content-value::text').get()
        jobitscraperItem['address'] = response.css('div.job-description__item--content div ::text').get()
        jobitscraperItem['time'] = response.css('div.job-detail__info--deadline::text').get()
        jobitscraperItem['rank'] = table_info[0].css('div.box-general-group-info-value ::text').get()
        jobitscraperItem['experience'] = table_info[1].css('div.box-general-group-info-value ::text').get()
        jobitscraperItem['number_of_recruits'] = table_info[2].css('div.box-general-group-info-value ::text').get()
        jobitscraperItem['working_form'] = table_info[3].css('div.box-general-group-info-value ::text').get()
        jobitscraperItem['sex'] = table_info[4].css('div.box-general-group-info-value ::text').get()
        jobitscraperItem['company'] = response.css('h2.company-name-label a ::text').get()
        jobitscraperItem['description'] = description[0].css('div.job-description__item--content li ::text').get()
        jobitscraperItem['requirements'] = description[1].css('div.job-description__item--content li ::text').get()
        jobitscraperItem['benefit'] = description[2].css('div.job-description__item--content p ::text').get()
        jobitscraperItem['url'] = response.url

        yield jobitscraperItem

