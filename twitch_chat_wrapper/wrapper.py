import socket
from events import Events


class TwitchChatWrapper:
    socket = None
    channel = ""
    readbuffer = b""
    bot_nickname = ""
    oauth_pass = ""

    def __init__(self, channel, bot_nickname, oauth_pass):
        events = Events(('on_ping', 'on_message'))
        events.on_ping += self.awake_notification
        self.events = events

        self.channel = channel
        self.bot_nickname = bot_nickname
        self.oauth_pass = oauth_pass

        self.socket = self.connect()

    @staticmethod
    def _socket_send(socket, string):
        socket.send(bytes(string, 'utf8'))

    def connect(self):
        _socket = socket.socket()
        _socket.connect(("irc.twitch.tv", 6667))
        self._socket_send(_socket, "PASS {}\r\n".format(self.oauth_pass))
        self._socket_send(_socket, "NICK {}\r\n".format(self.bot_nickname))
        self._socket_send(_socket, "JOIN #{} \r\n".format(self.channel))
        return _socket

    def send_message(self):
        self.socket.send("PRIVMSG #{} :{}\r\n".format(
            self.channel, message))

    def buffer_update(self):
        # this is a hack FIX IT
        try:
            readbuffer = bytes(self.readbuffer, 'utf-8') + self.socket.recv(1024)
        except:
            readbuffer = self.readbuffer + self.socket.recv(1024)
        temp = readbuffer.decode('utf-8').split("\n")
        self.readbuffer = temp.pop()
        return temp

    def awake_notification(self, line):
        if line[0] == "PING":
            server =  line[1]
            self.socket.send("PONG {}\r\n".format(server))

    def loop(self):
        MODT = False
        while True:
            temp = self.buffer_update()
            for line in temp:
                self.events.on_ping(line)
                parts = line.split(":")
                if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                    try:
                        message = parts[2][:len(parts[2]) - 1]
                    except:
                        message = ""
                    usernamesplit = parts[1].split("!")
                    username = usernamesplit[0]
                    if MODT:
                        self.events.on_message(username, message)
                       
                    for l in parts:
                        if "End of /NAMES list" in l:
                            MODT = True