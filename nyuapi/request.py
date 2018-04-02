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
        try:
            req = R.get("https://sandbox.api.it.nyu.edu/course-catalog-exp/", headers={
                "Authorization": "Bearer " + self.TOKEN
            }, timeout=10)
        except R.exceptions.ReadTimeout:
            raise Exception("[Error] NYU API not responding!")
        if req.text.find("Invalid or missing token") > -1:
            raise Exception("[Error] Token is not valid!")

    def rawReq(self, uri="", params={}):
        print("A request has been sent.")
        try:
            req = R.get(self.BASEURI + uri, data=params, headers={
                "Authorization": "Bearer " + self.TOKEN
            }, timeout=10)
        except R.exceptions.ReadTimeout:
            raise Exception("[Error] NYU API not responding!")
        return req.json()

    def repeatReq(self, url="", params={}):
        """
        server will send request repeatedly until valid response is received.
        However, if token invalid msg keep appearing, the server will halt.
        Therefore, a server monitor is needed.
        """ 
        counter = 0
        while 1:
            response = self.rawReq(url, params)
            counter += 1
            if isinstance(response, list):
                break
            if counter > 10:
                self.ping()
        return response
