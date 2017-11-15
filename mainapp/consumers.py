from channels import Group
from channels.sessions import channel_session


@channel_session
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    Group("chat").send({
        "text": message.content['reply_channel'] + ': ' + message['text'],
    })

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
