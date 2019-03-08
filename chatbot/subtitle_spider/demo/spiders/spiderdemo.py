# -*- coding: utf-8 -*-


import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatpItem

class MatplotSpider(scrapy.Spider):
    name = "matplot"
    allowed_domains = ["matplotlib.org"]
    start_urls = ['http://www.zimuzu.io/subtitle?page=2&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=3&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=4&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=5&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=6&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=7&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=8&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=9&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=10&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=11&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=12&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=13&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=14&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=15&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=16&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=17&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=18&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=19&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=20&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=21&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=22&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=23&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=24&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=25&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=26&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=27&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=28&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=29&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=30&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=31&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=32&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=33&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=34&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=35&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=36&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=37&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=38&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=39&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=40&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=41&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=42&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=43&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=44&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=45&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=47&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=46&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=48&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=49&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=50&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=51&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=52&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=53&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=54&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=55&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=56&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=57&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=58&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=59&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=60&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=61&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=62&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=63&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=64&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=65&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=66&category=&format=&lang=&sort=',
                  'http://www.zimuzu.io/subtitle?page=67&category=&format=&lang=&sort=',

                  ]

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.box.subtitle-list li',deny='/index.html$')
        print(len(le.extract_links(response)))

        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_linkto,dont_filter=True)


    def parse_linkto(self,response):
        href = response.css('div.subtitle-links.tc a::attr(href)').extract_first()
        print("gethere1")
        #href = LinkExtractor(restrict_css='div.clearfix a.down1',attrs='href')
        url = response.urljoin(href)
        request = scrapy.Request(href, callback=self.parse_link,dont_filter=True)
        #print("这是链接：", url)
        #print("这是链接：", href)
        yield request

    def parse_link(self,response):
        href = response.css('div.download-box a::attr(href)').extract_first()
        #print("这是链接：", href)
        url = response.urljoin(href)
        matpl = MatpItem()
        matpl['file_urls'] = [url]
        yield matpl
