import os
import scrapy

class AppPermissionsScrapper(scrapy.Spider):
    name="AppPermissionsScrapper"
    url = 'https://developer.android.com/reference/android/Manifest.permission.html'
    
    def start_requests(self):
        tag = getattr(self, 'url', None)
        if tag is not None:
            url = tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        lines = response.xpath('//table[@id="constants"]//tr//td//code//a')
        for index, link in enumerate(lines):
            z = (link.xpath("text()"))
            if z.get() != "String" and z.get().isupper():
                print(z.get())
                f=open("permissions_list.txt", "a+")
                f.write(z.get()+"\n")
                f.close()
