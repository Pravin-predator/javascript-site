import scrapy
from selenium import webdriver



class CountriesSpiderSpider(scrapy.Spider):
    name = "countries_spider"
    def start_requests(self):
        url = "https://quotes.toscrape.com/scroll"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get("https://quotes.toscrape.com/scroll")
        quote = driver.find_elements_by_class_name("quote")
        for country in quote:
            yield {
                "quote": country.text
            }


        driver.quit()
