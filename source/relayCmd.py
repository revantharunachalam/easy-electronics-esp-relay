from relaySerial import RelaySerial, read_command_line_arg

# Getting relay number and relay state
relay, state = read_command_line_arg()

# Formatting commad
command = "RELAY{0} {1}".format(relay, state)

# Relay operation
rsObj = RelaySerial(7, 9600)
rsObj.send_command(command)
del rsObj
