import requests as R


class reqNYU():

    TOKEN = ""
    BASEURI = "https://sandbox.api.it.nyu.edu/"

    def __init__(self, token=""):
        if not token:
            raise Exception("[Error] Token can not be empty!")
        self.TOKEN = token
        self.ping()
    
    def ping(self):
        req = R.get("https://sandbox.api.it.nyu.edu/course-catalog-exp/", headers={
            "Authorization": "Bearer " + self.TOKEN
        })
        if req.text.find("Invalid or missing token") > -1:
            raise Exception("[Error] Token is not valid!")

    def rawReq(self, uri="", params={}):
        print("A request has been sent.")
        req = R.get(self.BASEURI + uri, data=params, headers={
            "Authorization": "Bearer " + self.TOKEN
        })
        return req.json()

