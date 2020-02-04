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


class Middleware01:

    def __init__(self):
        pass

    def process_request(self, request):
        request.setname("|Row1_request|")
        return request

    def process_response(self, request, response):
        response.setresult("|Row1_response|")
        return request, response


class Middleware02:

    def __init__(self):
        pass

    def process_request(self, request):
        request.setname("|Row2_request|")
        return request

    def process_response(self, request, response):
        response.setresult("|Row2_response|")
        return request, response


midds = [Middleware01(), Middleware02()]

request = Request("request1")
print(request.getname())  # request1

for midd in midds:
    request = midd.process_request(request)

result = request.getname()
print(result)  # request1|Row1_request||Row2_request|


response = Response(result)
print(response.getresult())  # request1|Row1_request||Row2_request|


for midd in midds:
    request, response = midd.process_response(request, response)

print(request.getname())  # request1|Row1_request||Row2_request|
print(response.getresult())  # request1|Row1_request||Row2_request||Row1_response||Row2_response|
