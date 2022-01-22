import json
import scrapy

from ..items import CafebazaarItem


class CafeBazaarSpider(scrapy.Spider):
    name = "cafeBazaarspider"
    start_urls = []
    base_url = "https://api.cafebazaar.ir/rest-v1/process/AppDetailsV2Request"
    global_counter = 0

    def start_requests(self):
        yield scrapy.FormRequest(
            self.base_url,
            method="POST",
            callback=self.parse,
            body=self.get_request_body("com.nbadigital.gametimelite"),
        )

    def get_request_body(self, package_name: str) -> str:
        return json.dumps(
            {
                "properties": {
                    "language": 2,
                    "clientVersion": "web",
                },
                "singleRequest": {"appDetailsV2Request": {"packageName": package_name}},
            }
        )

    def parse(self, response):
        apps_rows = response.json()["singleReply"]["appDetailsV2Reply"][
            "extraContentPageBodyInfo"
        ]["pageBody"]["rows"]
        for i in apps_rows:
            for j in i["simpleAppList"]["apps"]:
                yield CafebazaarItem(
                    package_name=j["info"]["packageName"], rating=j["info"]["rate"]
                )

                yield scrapy.Request(
                    self.base_url,
                    method="POST",
                    callback=self.parse,
                    body=self.get_request_body(j["info"]["packageName"]),
                )
