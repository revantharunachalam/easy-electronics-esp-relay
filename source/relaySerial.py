import serial
import time
import argparse

class RelaySerial:
    def __init__(self, COMN: int=7, BaudRate: int=9600, timeout: int=4) -> None:
        """
        Set up the serial connection (adjust COM port and baud rate as necessary)
        """
        try:
            self.serial = serial.Serial('COM' + str(COMN), BaudRate, timeout=timeout)
        except:
            print("Close all the Serial terminals (Arduino Serial monitor or Terterm or Mobaxterm etc.) and try again...")
        time.sleep(1) # Wait for Arduino to initialize

    def send_command(self, command: str) -> None:
        """
        Send command to nodeMCU
        """
        self.serial.write(command.encode())
        print(f"Sent: {command}")

    def __del__(self) -> None:
        """
        Delete the pyserial object
        """
        self.serial.close()

def read_command_line_arg():
    """
    Hadnling commandline arguments
    """
    # Creating a prrser
    parser = argparse.ArgumentParser(description="Controlling the relay using esp8266")

    # add arguments
    parser.add_argument("-r", "--relay", help="Relay number", type=str, default="1")
    parser.add_argument("-s", "--state", help="State of relay", type=str, default="OFF")

    # Parsing arguments
    args = parser.parse_args()

    return args.relay, args.state