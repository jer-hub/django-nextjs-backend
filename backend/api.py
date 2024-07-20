from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("waitlist/", "waitlist.api.router")

@api.get("")
def hello(request):
    return "Hello World"