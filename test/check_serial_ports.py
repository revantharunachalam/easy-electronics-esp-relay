import serial.tools.list_ports

def list_open_com_ports():
    ports = serial.tools.list_ports.comports()
    open_ports = [port.device for port in ports]
    
    if open_ports:
        return open_ports
    else:
        print("No COM ports found.")
        return None