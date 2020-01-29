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
            response = self.process_response(request, response)
        return response

class Row1(MiddlewareMixin):

    def process_request(self,request):
        print("Row1_request")

    def process_response(self,request,response):
        print("Row1_response")
        return response

class Row2(MiddlewareMixin):

    def process_request(self,request):
        print("Row2_request")

    def process_response(self,request,response):
        print("Row2_response")
        return response

class Row3(MiddlewareMixin):

    def process_request(self,request):
        print("Row3_request")

    def process_response(self,request,response):
        print("Row3_response")
        return response

request = Request("request1")

result = request.getresponse()

response = Response(result)

print response.getresult() # response_request1
