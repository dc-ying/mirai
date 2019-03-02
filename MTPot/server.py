import socket
import logging

ServerLogger = logging.getLogger("HoneyPot")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ConsoleHandler = logging.StreamHandler()
ConsoleHandler.setFormatter(formatter)
FileHandler = logging.FileHandler('HoneyPot.log')
FileHandler.setFormatter(formatter)
ServerLogger.addHandler(ConsoleHandler)
ServerLogger.addHandler(FileHandler)
ServerLogger.setLevel(logging.INFO)
ServerLogger.info('HoneyPot is now working ...')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 5555))
ServerLogger.info('Bind UDP on 5555 ...') 
while True:
	data, addr = s.recvfrom(1024)
	ServerLogger.info(data)
s.close()
