# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

data = []


class CafebazaarPipeline:
    def process_item(self, item, spider):
        if item not in data:
            data.append(item)
        return item

    def close_spider(self, spider):
        with open("cafeBazaarData.text", "w+") as file:
            for i in data:
                file.write(f"{i['package_name']} | {i['rating']}\n")
