#!/usr/bin/env python3

from scrapy import cmdline

if __name__ == '__main__':
    spider = 'avito_ru'
    cmdline.execute(f"scrapy crawl {spider}".split())


