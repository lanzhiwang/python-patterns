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

class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            request, response = self.process_response(request, response)
        return request, response

class Middleware01(MiddlewareMixin):

    def __init__(self, get_response=None):
        pass

    def process_request(self, request):
        request.setname("|Row1_request|")
        return request

    def process_response(self, request, response):
        response.setresult("|Row1_response|")
        return request, response

class Middleware02(MiddlewareMixin):

    def __init__(self, get_response=None):
        pass

    def process_request(self, request):
        request.setname("|Row2_request|")
        return request

    def process_response(self, request, response):
        response.setresult("|Row2_response|")
        return request, response

midds = [Middleware01, Middleware02]

request = Request("request1")
response = None
for midd in midds:
    request, response = midd(request)

print response.getresult()
