TwitchChatWrapper
-----------------

This is a simple twitch chat wrapper written on python that I use to build simple bots fast.


# installation

```
pip intall twitch_chat_wrapper
```

# fetchin Twitch oauth password token

Follow this link https://twitchapps.com/tmi/ and save the token

# usage

```python
from twitch_chat_wrapper import TwitchChatWrapper

viewers_greetings = []

def message_handler(chat, username, message):
    print("@{}: {}".format(username, message))
    if username not in viewers_greetings:
        chat.send_message("@{} welcome to the stream".format(username))
        viewrs_greetings.append(username)


twitch = TwitchChatWrapper(
    bot_nickname="AwesomeBot", 
    oauth_pass="oauth:r1xxk1111111111112222222222xwd", 
    channel="hardlydifficult") 

twitch.events.on_message += message_handler

twitch.loop()
```

# shout out

To https://www.twitch.tv/hardlydifficult which is building a awesome gamedev twitch community