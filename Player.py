from pylgbst import *
from pylgbst.comms import DebugServerConnection
from time import sleep

from pylgbst.hub import MoveHub
from pylgbst import get_connection_auto
from pylgbst.hub import MoveHub



class Player:
    def __init__(self):
        conn = GattConnection()
    try:
        conn.connect()
        hub = MoveHub(conn)

    def handlerevent(self, event):
        print(" ")
