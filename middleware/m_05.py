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


class RegistryHolder(type):

    REGISTRY = []

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)  # new_cls = super(RegistryHolder, cls).__new__(cls, name, bases, attrs)
        cls.REGISTRY.append(new_cls)
        return new_cls

    @classmethod
    def get_registry(cls):
        return cls.REGISTRY


class Middleware(metaclass=RegistryHolder):
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def __call__(self):
        for midd in RegistryHolder.get_registry():
            if midd(self.request, self.response).__class__.__name__ == self.__class__.__name__:
                continue
            midd(self.request, self.response).process_request()

        self.response = Response(self.request.getname())

        for midd in RegistryHolder.get_registry():
            if midd(self.request, self.response).__class__.__name__ == self.__class__.__name__:
                continue
            midd(self.request, self.response).process_response()
        return self.request, self.response


class Middleware01(Middleware):
    def process_request(self):
        self.request.setname("|Row1_request|")

    def process_response(self):
        self.response.setresult("|Row1_response|")


class Middleware02(Middleware):
    def process_request(self):
        self.request.setname("|Row2_request|")

    def process_response(self):
        self.response.setresult("|Row2_response|")


request = Request("request1")
response = None
midd = Middleware(request, response)
request, response = midd()
print(response.getresult())
