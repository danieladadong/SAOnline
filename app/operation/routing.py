from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.operation.consumers import ChatConsumer
websocket_urlpatterns = [
	path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),  # 这里可以定义自己的路由
]
