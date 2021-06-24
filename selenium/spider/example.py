import scrapy
from selenium import webdriver



class QuotesSpider(scrapy.Spider):
    name = "example"
    def start_requests(self):
        url = "https://quotes.toscrape.com/scroll"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get("https://quotes.toscrape.com/scroll")
        quote = driver.find_elements_by_class_name("quote")
        for qt in quote:
            yield {
                "quote": qt.text
            }


        driver.quit()
