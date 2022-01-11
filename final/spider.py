import scrapy
import requests


class NBASpider(scrapy.Spider):
    name = "blogspider"
    start_urls = ["https://api.cafebazaar.ir/rest-v1/process/AppDetailsV2Request"]

    def parse(self, response):
        for title in response.css(".oxy-post-title"):
            yield {"title": title.css("::text").get()}

        for next_page in response.css("a.next"):
            yield response.follow(next_page, self.parse)
