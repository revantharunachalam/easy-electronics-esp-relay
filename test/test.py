import sys
import os
import unittest
from unittest.mock import patch, MagicMock
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from relaySerial import RelaySerial

class TestRelaySerial(unittest.TestCase):
    """
    Testcase from ChatGPT for testing relaySerial class.
    """

    @patch('serial.Serial')  # Mock the serial.Serial class
    def test_initialization(self, mock_serial):
        # Mock the Serial object
        mock_serial_instance = MagicMock()
        mock_serial.return_value = mock_serial_instance
        
        # Initialize the RelaySerial class
        relay_serial = RelaySerial(COMN=5, BaudRate=115200, timeout=2)
        
        # Check if Serial was initialized with the correct parameters
        mock_serial.assert_called_once_with('COM5', 115200, timeout=2)

        # Ensure there's a sleep call for initialization wait
        time.sleep(1)  # Simulate the sleep, doesn't need to be checked here

    @patch('serial.Serial')
    def test_send_command(self, mock_serial):
        # Mock the Serial object
        mock_serial_instance = MagicMock()
        mock_serial.return_value = mock_serial_instance
        
        # Initialize RelaySerial object
        relay_serial = RelaySerial()
        
        # Send a command
        command = "ON"
        relay_serial.send_command(command)
        
        # Check if the command was encoded and sent through serial
        mock_serial_instance.write.assert_called_once_with(command.encode())
        print(f"Expected: Sent: {command}")

    @patch('serial.Serial')
    def test_cleanup(self, mock_serial):
        # Mock the Serial object
        mock_serial_instance = MagicMock()
        mock_serial.return_value = mock_serial_instance
        
        # Create the RelaySerial object and immediately delete it
        relay_serial = RelaySerial()
        del relay_serial
        
        # Check if the serial connection was closed
        mock_serial_instance.close.assert_called_once()

    @patch('serial.Serial')
    def test_serial_initialization_failure(self, mock_serial):
        # Simulate failure in serial port initialization
        mock_serial.side_effect = Exception("Serial connection failed")
        
        # Capture print statement output
        with self.assertLogs(level='INFO') as log:
            relay_serial = RelaySerial()
            self.assertIn("Close all the Serial terminals", log.output)

if __name__ == '__main__':
    unittest.main()