import requests
from urllib import parse

import locations


class Location:
    def __init__(self, locator=locations.config.Amap):
        """
        :param locator: 默认采用高德地图，可选参数：
        amap：高德地图
        baidu：百度地图
        """
        self.locator = locator
        self.amapBaseUrl = "https://restapi.amap.com/v3/geocode/geo?address={}&output={}&key={}"
        self.baidumapBaseUrl = "https://api.map.baidu.com/geocoding/v3/?address={}&output={}&ak={}"

    def locate(self, address: str):
        """
        :param address: 要采集的地址
        :return:
        """
        if isinstance(self.locator(), locations.config.Amap):
            final_url = self.amapBaseUrl.format(address, self.locator.OUTPUT, self.locator.KEY)
            req = requests.get(url=final_url)
            if req.status_code == 200:
                content = req.json()
                location = content["geocodes"][0]["location"]
                return location

        final_url = self.baidumapBaseUrl.format(address, self.locator.OUTPUT.lower(), self.locator.KEY)
        req = requests.get(url=final_url)
        if req.status_code == 200:
            content = req.json()
            location = content["result"]['location']
            return location
