#coding=utf-8
import requests
from lxml import etree
import json

if __name__ == "__main__":
    url = "https://flights.ctrip.com/international/search/api/lowprice/calendar/get45DaysCalendarDetailList?v=0.2518945922379514"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Content-type" : "application/json;charset=UTF-8"
    }
    data = {
        "flightSegmentList":
        [
            {
                "arrivalCityCode":"BJS",
                "departureCityCode":"SIA",
                "departureDate":"2021-03-28"
            },
            {
                "arrivalCityCode":"SIA",
                "departureCityCode":"BJS",
                "departureDate":"2021-04-28"
            }],
            "cabin":"Y_S_C_F",
            "flightWay":"D"
    }
    response = requests.post(url=url, data=data, headers = headers).text
    print(response)