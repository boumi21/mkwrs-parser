# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta

#Date format : (yyyy, mm, dd)
startDate = date(2008, 0o4, 12)   # start date
endDate = date(2020, 1, 31)       # end date


class MkwrsParserSpider(scrapy.Spider):
    name = 'mkwrs_parser'

    delta = endDate - startDate       # as timedelta
    dateList = []

    for i in range(delta.days + 1):
        day = startDate + timedelta(days=i)
        dateList.append(day)

    # List of URL's
    start_urls = ['https://mkwrs.com/mkwii/wrs.php?date={0}'.format(day) for day in dateList]




    def parse(self, response):      
        domText = response.xpath('//*[@id="main"]/table/tr/td[2]/b//text()').get()
        #yield { 'date': response.request.url[-10:], 'minutes': domText[:2], 'seconds': domText[3:5], 'milliseconds': domText[-3:]}
        #yield { 'date': response.request.url[-10:], 'time': '00:'+domText}
        yield { 'date': response.request.url[-10:], 'time': ( int(domText[:2]) * int(60000)   ) + ( int(domText[3:5]) * int(1000) ) + (int(domText[-3:]))}
