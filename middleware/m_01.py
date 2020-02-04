class Request:
    def __init__(self, name):
        self.name = name

    def getresponse(self):
        return "response_" + self.name


class Response:
    def __init__(self, result):
        self.result = result

    def getresult(self):
        return self.result


request = Request("request1")

result = request.getresponse()

response = Response(result)

print(response.getresult())  # response_request1
