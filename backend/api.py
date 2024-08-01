from ninja import NinjaAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("waitlist/", "waitlist.api.router")

@api.get("")
def hello(request):
    return "Hello World"