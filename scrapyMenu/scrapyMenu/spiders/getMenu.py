from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapyMenu.items import ScrapymenuItem
from bs4 import BeautifulSoup
import logging

class MySpider(CrawlSpider):
    name = "menu"

    allowed_domains = ["uhouzz.com"]
    start_urls = ["https://www.uhouzz.com/us-uk/london/apartments"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="current next"]'), follow= True),
        Rule(LinkExtractor(deny=('')), callback="parse_items"))
        )

    def parse_items(self, response):
        # hxs = HtmlXPathSelector(response)
        # titles = hxs.xpath('//span[@class="pl"]')

        sopa = BeautifulSoup(response.text, 'lxml')
        # logging.error(sopa)
        current_link = ''

        for link in sopa.find_all('a','title'):
            current_link = link.get('href')
            logging.error(current_link)
            # if current_link.endswith('pdf'):
                # logging.error(current_link)
            item = ScrapymenuItem()
            item["title"] = self.allowed_domains
            item["link"] = current_link
            yield item



        # for titles in titles:
        #     item = ScrapymenuItem()
        #     item["title"] = titles.xpath("a/text()").extract()
        #     item["link"] = titles.xpath("a/@href").extract()
        #     items.append(item)

        return
