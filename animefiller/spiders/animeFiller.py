import scrapy
from animefiller.items import AnimefillerItem


class AnimeFiller(scrapy.Spider):
    name = "animefiller"
    start_urls = ["https://www.animefillerlist.com/shows/"]

    def parse(self, response):
        for url in response.css(".Group ul li"):
            url = "https://www.animefillerlist.com" + \
                url.css("a::attr(href)").get()
            yield scrapy.Request(url, callback=self.parseShow)

    def parseShow(self, response):
        for episode in response.css("table tbody tr"):
            item = AnimefillerItem()
            item['anime'] = episode.xpath(
                '//*[@id="block-afl-general-breadcrumb"]/div/div/text()[2]').get()[2:].strip()
            item['number'] = episode.css(".Number::text").get()
            item['title'] = episode.css(".Title a::text").get()
            item['type'] = episode.css(".Type span::text").get()
            item['date'] = episode.css(".Date::text").get()
            yield item
