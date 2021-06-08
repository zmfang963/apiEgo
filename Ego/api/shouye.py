import requests
class Ego_SY_Api:
    def __init__(self):
        self.get_banner_url="http://e.cn/api/v1/banner/1"
        self.get_theme_url = "http://e.cn/api/v1/theme?ids=1"
        self.get_product_recent_url = "http://e.cn/api/v1/product/recent"
        self.get_category_url = "http://e.cn/api/v1/category/all"
    def get_banner(self):
        return requests.get(url=self.get_banner_url)
    def get_theme(self):
        return requests.get(url=self.get_theme_url)
    def get_product_recent(self):
        return requests.get(url=self.get_product_recent_url)
    def get_category(self):
        return requests.get(url=self.get_category_url)