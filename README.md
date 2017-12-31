TwitchChatWrapper
-----------------

This is a simple twitch chat wrapper written on python that I use to build simple bots fast.


# installation

```
pip intall twitch_chat_wrapper
```

# fetchin Twitch oauth password token

Follow this link https://twitchapps.com/tmi/ and save the token

# usuage

```
from twitch_chat_wrapper import TwitchChatWrapper


def message_handler(username, message):
    print(username, message)


twitch = TwitchChatWrapper(
    bot_nickname="AwesomeBot", 
    oauth_pass="oauth:r1xxk1111111111112222222222xwd", 
    channel="hardlydifficult") 

twitch.events.on_message += message_handler

twitch.loop()
```

#shout out

To https://www.twitch.tv/hardlydifficult which is building a awesome gamedev twitch community