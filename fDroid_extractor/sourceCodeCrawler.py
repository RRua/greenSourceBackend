# -*- coding: utf-8 -*-
import os
import scrapy

class SourceCodeScrapper(scrapy.Spider):
    name = 'https://f-droid.org/'

    def start_requests(self):
        url = ''
        tag = getattr(self, 'url', None)
        if tag is not None:
            url = tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        url = response.xpath('//p[@class="package-version-source"]//a/@href').get()
        header = response.xpath('//header[@class="package-header"]')
        description = header.xpath('//div[@class="package-description"]//p/text()').get()
        summary = header.xpath('//div[@class="package-summary"]/text()').get()
        pack_name = header.xpath('//h3[@class="package-name"]/text()').get()
        icon_url =  header.xpath('//img[@class="package-icon"]/@src').get()
        jso = {}
        jso['url'] = url
        jso['summary'] = summary.strip()
        jso['icon_url'] = icon_url
        jso['pack_name'] = pack_name.strip()
        jso['description'] = description
        return jso

