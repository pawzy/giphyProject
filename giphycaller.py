from __future__ import print_function
import time
import json
import ast
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


class GiphyCaller:
    def __init__(self, tag, format='json', rating='g'):
        self.tag = tag
        self.rating = rating
        self.format = format
        self.apiInstance = giphy_client.DefaultApi()
        self.apiKey = 'pIxY5SeVYIdXrIxsIFqQnpZMRPesMZux'
        self.logFile = 'sentGifs.txt'
    def getRandom(self):
        try:
            apiResponse = self.apiInstance.gifs_random_get(self.apiKey, tag=self.tag, rating=self.rating,
                                                           fmt=self.format)
            giphyURL = json.loads(json.dumps(ast.literal_eval(str(apiResponse))))['data']['image_url']

            try:
                with open(self.logFile, 'a') as f:
                    f.write("asd")
            except Exception as e:
                print("Issues with opening file ", e)

            print(giphyURL)
            # print(type(apiResponseText))
            # giphyUrl = json.dumps(apiResponseText)
            # print(giphyUrl)
            # pprint(apiResponse)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

    def checkIfRandomAlreadySent(self):
        pass
