import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



class ExampleSpider(scrapy.Spider):
    name = 'example'
    def start_requests(self):
        url = 'https://quotes.toscrape.com/scroll/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get('https://quotes.toscrape.com/scroll/')
        driver.implicitly_wait(10)
        quotes = driver.find_elements_by_css_selector("div.quote")
        for qt in quotes:
            yield{
                'text': driver.find_element_by_css_selector('span.text::text').get()
            }




