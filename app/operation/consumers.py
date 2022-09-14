import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from app.users.models import UserProfile
from channels.db import database_sync_to_async
from app.operation.models import UserMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = str(self.room_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,#每个用户是一个组的话可以实现只发送到特定的人
            self.channel_name
        )
        await self.accept()
        print(self.room_group_name)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        fromuser = text_data_json['uuid']
        touser = text_data_json['touuid']
        message = text_data_json['message']
        nick_name = text_data_json['username']
        # Send message to room group
        await self.channel_layer.group_send(
            str(touser),
            {
                'type': 'chat_message',
                'message': message,
                'username':nick_name,
                'uuid':fromuser,
                'touuid':touser
            }
        )


    @database_sync_to_async
    def get_userinfo(self,id):
        return UserProfile.objects.get(id=id)

    # Receive message from room group
    async def chat_message(self, event):
        message =  event['message']
        nick_name = event['username']
        fromuser = event['uuid']
        touser = event['touuid']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'code':200,
            'username': nick_name,
            'message': message,
            'uuid':fromuser,
            'touuid':touser
        }))