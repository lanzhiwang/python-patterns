class Request:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setname(self, value):
        self.name += value

class Response:
    def __init__(self, result):
        self.result = result

    def getresult(self):
        return self.result

    def setresult(self, value):
        self.result += value


class Middleware:

    def __init__(self):
        pass

    def process_request(self, request):
        request.setname("|Row_request|")
        return request

    def process_response(self, request, response):
        response.setresult("|Row_response|")
        return request, response


midd = Middleware()

request = Request("request")
print request.getname() # request

request = midd.process_request(request)
print request.getname() # request|Row_request|

result = request.getname()
print result # request|Row_request|

response = Response(result)
print response.getresult() # request|Row_request|

request, response = midd.process_response(request, response)
print response.getresult() # request|Row_request||Row_response|

print response.getresult() # request|Row_request||Row_response|
