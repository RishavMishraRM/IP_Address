# Python Program to Get IP Address of website
import socket
url="www.github.com"
print("IP:",socket.gethostbyname(url))