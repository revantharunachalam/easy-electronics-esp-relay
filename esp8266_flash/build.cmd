@echo off

REM Initialize configuration file and find esp8266
echo Initialize configuration file and find esp8266
arduino-cli config init --overwrite --dest-file esp8266_flash-cli.yaml
arduino-cli config add board_manager.additional_urls http://arduino.esp8266.com/stable/package_esp8266com_index.json
arduino-cli core update-index --config-file esp8266_flash-cli.yaml
arduino-cli core search esp8266 --config-file esp8266_flash-cli.yaml
echo ----------------------------------------------

REM Install platform
echo Install platform
arduino-cli board listall --config-file esp8266_flash-cli.yaml
arduino-cli core install esp8266:esp8266
echo ----------------------------------------------

REM Compile Sketch
echo Compile Sketch
rmdir /S /Q "1_build"
mkdir "1_build"
arduino-cli compile --fqbn esp8266:esp8266:nodemcu . --config-file esp8266_flash-cli.yaml --output-dir 1_build
echo ----------------------------------------------
