import socket
import string
from settings import HOST, PORT, PASS, IDENT
import time
import csv
import requests
import json
import re

class TwitchBot:
    '''
    Es la clase que se instancia para generar un bot de Twitch. Se le pasa el canal
    al cual se va aconectar porque podemos tener hasta 20 bots conectados con un 
    mismo oauth token. 
    '''

    def __init__(self, channel):
        '''
        Define las caracteristicas básicas para crear un bot que se conecta
        a Twitch a través de un IRC e inicializa el socket. 
        '''
        self.channel = channel
        self.stalk = False
        self.socket = self.openSocket()

        # Make the bot join a Room
        self.joinRoom()

    def openSocket(self):
        '''
        Configura un socket.
        '''
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))  # Enviamos el oauth token
        s.send(bytes("NICK " + IDENT + "\r\n", "UTF-8"))
        s.send(bytes("JOIN #" + self.channel + "\r\n", "UTF-8"))

        return s

    def joinRoom(self):
        '''
        Conectamos el bot a un canal el cual queremos revisar.
        '''
        readbuffer = ""
        Loading = True
        while Loading:
            readbuffer = readbuffer + self.socket.recv(1024).decode("UTF-8")
            temp = readbuffer.split("\n")
            readbuffer =temp.pop()

            for line in temp:
                print(line)
                Loading = self.loadingComplete(line)
        self.sendMessage("Hey! HeyGuys ")
        

    def loadingComplete(self, line):
        '''
        Revisa que se haya unido satisfactoriamente al canal y que este cargando los mensajes del
        chat. EXTRA: Tambien le damos banderas de membresia y tags para que nos muestre más info 
        del usuario al que nos queremos conectar.
        '''

        if "End of /NAMES list" in line:
            self.socket.send(bytes("CAP REQ :twitch.tv/membership\r\n", "UTF-8"))
            self.socket.send(bytes("CAP REQ :twitch.tv/tags \r\n", "UTF-8"))
            return False

        else:
            
            return True

    def sendMessage(self, message):
        '''
        Da la codificación adecuada al string para enviarlo por el IRC al chat. Este solo sirve para 
        mensajes que se van mostrar en el chat pero no para comandos. 
        '''
        messageTemp = "PRIVMSG #" + self.channel + " :" + message
        self.socket.send(bytes(messageTemp + "\r\n", "UTF-8"))
        print("Sent: " + messageTemp)

    def receiveMessages(self):
        '''
        Lee los mensajes de entrada yd ecide que acción se debe realiza al respecto de cada 
        mensaje dependiendo de que es lo que el usuario quiere que haga. 
        '''

        while True: 
            message = self.socket.recv(2048).decode("UTF-8")
            message.strip('\n\r')
            print(message)

            # Stalk permite guardar la información del chat en un CSV.
            if self.stalk:
                data = [time.ctime(), self.getUserName(message), self.getMessage(message[:-1]), self.getBagde(message), self.getSubscribed(message) ]
                with open("chat_log.csv", 'a+') as log:
                    print(data)
                    writer = csv.writer(log)
                    writer.writerow(data)

            # Saluda a la Gente
            if 'Hola @juanpflores' in message.split(":")[2]:
                self.sendMessage("Hola @" + self.getUserName(message) + ", ¿Cómo Estas?")

            # Da las redes sociales del canal
            if '!social' in message.split(":")[2]:
                self.sendMessage("Sigue a Juan Pablo en: fb.com/juanpflores o también a traves de twitter Twitter: @jpflores9")

            # Da la hora del streamer.
            if '!time' in message.split(":")[2]:
                self.sendMessage("Son las {0} en CDMX.".format(time.ctime().split(' ')[3]))

            # Cuenta un chiste de Chuck Norris
            if '!chucknorris' in message.split(":")[2]:
                response = requests.get("http://api.icndb.com/jokes/random")
                joke = response.json()['value']['joke']
                self.sendMessage('Tengo un chiste para ti: {0}'.format(joke))

            if '!stalk' in message.split(":")[2]:
                self.stalk = not self.stalk
            

    def getUserName(self, message):
        return re.search('display-name=.*;emotes', message).group(0)[13:-7]


    def getMessage(self, message):
        return message.split(":")[2]

    def getBagde(self, message):
        res = re.search('=.*/', message)
        badge = res.group(0)[1:-1]
        return badge
    
    def getSubscribed(self, message):
        res = re.search('subscriber=.;', message)
        subs = res.group(0)[-2:-1]
        return subs

if __name__ == "__main__":
    channel_list = ['juanpflores']
    bot_list = []

    for channel in channel_list:
        bot = TwitchBot(channel)
        bot.receiveMessages()