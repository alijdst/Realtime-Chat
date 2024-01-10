from django.urls import path, include, re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
	path("<room_slug>" , ChatConsumer.as_asgi()),
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
]












# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.urls import path
#
# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#
#         )
#     )
# })