@REM Initialize configuration file
arduino-cli config init --overwrite --dest-file esp8266_flash-cli.yaml

@REM Creating new sketch (.ini file)
arduino-cli sketch new .

@REM Display the list of boards
arduino-cli board list --config-file esp8266_flash-cli.yaml

@REM Searching ESP8266
arduino-cli core search esp8266 --config-file esp8266_flash-cli.yaml

@REM Updating index which has ESP8266 related files (Need to add https://arduino.esp8266.com/stable/package_esp8266com_index.json in config file)
arduino-cli core update-index --config-file esp8266_flash-cli.yaml

@REM Listing all the boards after updating index
arduino-cli board listall --config-file esp8266_flash-cli.yaml

@REM Clean build directory
del /q 1_build
mkdir 1_build

@REM Compile .ino file
arduino-cli compile --fqbn esp8266:esp8266:nodemcu . --config-file esp8266_flash-cli.yaml --output-dir 1_build

@REM Flash ESP8266 binary
arduino-cli upload --port COM7 --input-dir 1_build --fqbn esp8266:esp8266:nodemcu . --config-file esp8266_flash-cli.yaml