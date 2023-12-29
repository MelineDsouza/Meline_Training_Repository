import json
# from urllib.parse import urljoin
import jsonpath
# import requests
import random
from ApiSimpleBooks.commonMethods import *
class SimpleBooks:
    def Authenticate(self):
        global token
        global id

        response = commMethods.post_requests(self,baseurl,resource["Authorization"],authoriz)
        print(response.status_code)
        token = commMethods.load_Json(self, response, 'accessToken')
        print(token)

    def order(self):
        global id
        print("112rtfdsdfgh")
        print(token[0])
        Authheaders = {'Authorization': 'Bearer ' + token[0]}
        response = requests.post(urljoin(baseurl, resource["orderResource"]), json=createBoard, headers=Authheaders)
        print(response.status_code)
        id = commMethods.load_Json(self, response, 'orderId')
        print(id)

    def getaBook(self):
        Aheaders = {'Authorization': 'Bearer ' + token[0]}
        response = requests.get(urljoin(baseurl, resource["getBook"]+id[0]), Aheaders)
        print(response.status_code)
        print(response.json())

    def updateAnOrder(self):
        resource = "/orders/" + id[0]
        headers = {'Authorization': 'Bearer ' + token[0]}
        response = commMethods.update_request(self,baseurl, resource["getBook"]+id[0], postboxy, header=headers)
        print(response.status_code)



    def deleteorder(self):
        baseUrl = "https://simple-books-api.glitch.me/"
        resource = "/orders/"+id[0]
        headers = {'Authorization': 'Bearer ' + token[0]}
        response = requests.delete(urljoin(baseUrl, resource), headers=headers)
        print(response.status_code)


obj = SimpleBooks()
obj.Authenticate()
obj.order()
# obj.getaBook()
# obj.updateAnOrder()
# obj.deleteorder()
