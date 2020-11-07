![image](https://github.com/mytechnotalent/CircuitPython_IoT_Streaming_Data_ESP32-S2_OLED_Version/blob/main/CircuitPython%20IoT%20Streaming%20Data%20ESP32-S2%20OLED%20Version.png?raw=true)

# CircuitPython IoT Streaming Data ESP32-S2 OLED Version
An IoT Streaming Data app that shows you how to take a JSON web API such as the FREE Hacker News API and stream and display it on a Metro ESP32-S2 in an OLED display.

* This code is based on a collaborative effort between @mytechnotalent on Twitter, mytechnotalent on GitHub, @MakeMyAndroidAp on Twitter, FoamyGuy on GitHub and @anecdat on Twitter, anecdata on GitHub.  Original project [HERE](https://github.com/mytechnotalent/CircuitPython_IoT_Streaming_Data).

* This direct code is a collaborative effort between @mytechnotalent on Twitter, mytechnotalent on GitHub, @MakeMyAndroidAp on Twitter, FoamyGuy on GitHub.

## Schematic
![image](https://github.com/mytechnotalent/CircuitPython_IoT_Streaming_Data_ESP32-S2_OLED_Version/blob/main/schematic.png?raw=true)

## Parts
[Adafruit Metro ESP32-S2](https://www.adafruit.com/product/4775)<br>
[0.96'' I2C IIC 12864 128X64 Pixel OLED LCD Display](https://www.amazon.com/IZOKEE-Display-SSD1306-Raspberry-White-IIC/dp/B076PDVFQD)

## Installation
```bash
git clone https://github.com/mytechnotalent/CircuitPython_IoT_Streaming_Data_ESP32-S2_OLED_Version.git
```

## Copy Files From Repo To PyPortal OR PyPortal Pynt
```bash
lib\
code.py 
secrets.py
font5x8.bin
test_wrap_nicely.py [ORIGINAL SOURCE: https://github.com/adafruit/Adafruit_CircuitPython_PyPortal/blob/master/adafruit_pyportal.py]
unittest.py [SOURCE: https://github.com/micropython/micropython-lib/blob/master/unittest/unittest.py]
wrap_nicely.py
```

## STEP 1: Modify secrets.py
Edit the `secrets.py` file with your credentials.

## STEP 2: Review the Hacker News API
Take a few minutes and review the Hacker News API [HERE](https://github.com/HackerNews/API) and see how they explain their API and the endpoints to which you can connect.  After reviewing, look at the `code.py` within this repo and see how it is implemented.  Once you have an understanding of this you can apply any API to this example framework to make any kind of streaming app that you so chose.

## STEP 3: Power Device
This is the FUN part where you get to fire up your new streaming device!  

## 24/7 Community Of Support
If you have any questions regarding this app or implementing your own version of this app please visit us in the CircuitPython Discord channel [HERE](https://discord.com/invite/5FBsBHU) and visit the `help-with-circuitpython` room.

## Run Tests in REPL
```bash
import unittest
unittest.main('test_wrap_nicely')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
