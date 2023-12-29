import json
import random
from urllib.parse import urljoin

import jsonpath
import requests

baseurl = "https://simple-books-api.glitch.me/"
resource = {"Authorization" : "/api-clients/",
            "orderResource" : "/orders/",
            "getBook":"/orders/"}
num = str(random.randint(0, 100))

authoriz= {
            "clientName": "Meline" + num,
            "clientEmail": "Mel" + num + "@gmail.com"
        }
createBoard={
         "bookId": 2,
         "customerName": "Macline"
}
postboxy = {
            "customerName": "Amline"
           }
class commMethods:
    def post_requests(self,baseurl,resource,json_data):
        return requests.post(urljoin(baseurl,resource),json=json_data)

    def load_Json(self, response, data):
        res = json.loads(response.text)
        return jsonpath.jsonpath(res, data)

    def post_OrderReq(self,baseurl,resource,json_data2,header):
        return requests.post(urljoin(baseurl,resource),json=json_data2, headers=header)

    def update_request(self,baseurl,resource,json_data,header):
        return requests.post(urljoin(baseurl,resource),json=json_data, headers=header)
