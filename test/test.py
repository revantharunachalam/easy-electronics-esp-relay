import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from relaySerial import RelaySerial

rs = RelaySerial(7, 9600)
rs.send_command("RELAY2 OFF")
del rs