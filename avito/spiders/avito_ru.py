import scrapy


class AvitoRuSpider(scrapy.Spider):
    name = 'avito_ru'
    allowed_domains = ['avito.ru']
    start_urls = ['https://avito.ru/']

    def parse(self, response):
        items = response.xpath('//a/h3')
        for item in items:
            data = {
                'title': item.xpath('./text()').get(),
                'url': response.urljoin(item.xpath('./parent::*/@href').get()),
            }
            print(data)
