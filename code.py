import gc
import ipaddress
import wifi
import adafruit_requests
import time
import ssl
import socketpool
import board
import busio as io
from wrap_nicely import wrap_nicely
import adafruit_ssd1306

from secrets import secrets

def display_text(text, line):
    """Display text function
    Parameters
    ----------
    text : str
        Text to print
    line: int
        Line to print text on
    Returns
    -------
    None
    """
    oled.fill(0)
    text = str(text)
    oled.text(text, 0, line, 1)
    #oled.text('World', 0, 10)
    oled.show()


# Instantiate i2c object
i2c = io.I2C(board.SCL, board.SDA)

# Instantiate OLED object
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

# Setup wifi and connection
print(wifi.radio.connect(secrets['ssid'], secrets['password']))
print('ip', wifi.radio.ipv4_address)
ipv4 = ipaddress.ip_address('8.8.8.8')
print('ping', wifi.radio.ping(ipv4))
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Set up where we'll be fetching data from
DATA_SOURCE = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Perform a GET on the DATA_SOURCE and instantiate into a response object
print('Fetching DATA_SOURCE')

# Garbage collect before our GET request
gc.collect()

# Create our response and DATA objects
response = requests.get(DATA_SOURCE)
DATA = response.json()
response.close()

# Garbage collect after our GET request
gc.collect()

while True:
    try:
        # Cycle through articles
        for i in DATA:
            ARTICLE = 'https://hacker-news.firebaseio.com/v0/item/{0}.json'.format(i)
            gc.collect()
            print('Fetching ARTICLE')
            response = requests.get(ARTICLE)
            ARTICLE_JSON = response.json()
            response.close()
            gc.collect()
            print(ARTICLE_JSON['by'])
            display_text(ARTICLE_JSON['by'], 0)
            time.sleep(1)
            print(ARTICLE_JSON['score'])
            display_text(ARTICLE_JSON['score'], 0)
            time.sleep(1)
            print(ARTICLE_JSON['title'])
            # TODO: Foamy if you can fiture out how to only wrap nicely this 'title' on this 1306 screen thanks!
            display_text("\n".join(wrap_nicely(ARTICLE_JSON['title'], 18)), 0)
            time.sleep(10)
    except KeyboardInterrupt:
        break
    except Exception as e:
        # An RuntimeError in addition to other errors can occur if you lose
        # internet so reset the device
        print(e)
        print('Exception')
        import microcontroller
        microcontroller.reset()