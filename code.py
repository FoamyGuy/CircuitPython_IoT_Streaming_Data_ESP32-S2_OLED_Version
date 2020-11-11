import gc
import ipaddress
import wifi
import time
import ssl
import socketpool
import board
import terminalio
import displayio
import adafruit_requests
from adafruit_display_text import label
from wrap_nicely import wrap_nicely
import adafruit_displayio_ssd1306

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

    text = str(text)
    output_label.text = " "
    output_label.text = text


# Instantiate i2c object
i2c = board.I2C()

displayio.release_displays()
# Instantiate OLED object
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32, rotation=180)

output_label = label.Label(terminalio.FONT, color=0xFFFFFF, max_glyphs=30 * 4)
output_label.anchor_point = (0, 0)
output_label.anchored_position = (0, 0)

display.show(output_label)

# Setup wifi and connection
print(wifi.radio.connect(secrets['ssid'], secrets['password']))
print('ip', wifi.radio.ipv4_address)
display_text("ip: {}".format(wifi.radio.ipv4_address), 0)
ipv4 = ipaddress.ip_address('8.8.8.8')
ping_result = wifi.radio.ping(ipv4)
print('ping', ping_result)
display_text("ping: {}".format(ping_result), 0)
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Set up where we'll be fetching data from
DATA_SOURCE = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Garbage collect before our GET request
gc.collect()
suceed = False

while not suceed:
    # Perform a GET on the DATA_SOURCE and instantiate into a response object
    display_text('Fetching DATA_SOURCE', 0)
    print('Fetching DATA_SOURCE')
    try:
        # Create our response and DATA objects
        response = requests.get(DATA_SOURCE)
        DATA = response.json()
        response.close()
        suceed = True
    except OSError as e:
        print(e)
        display_text("OS Error. Retrying", 0)
        time.sleep(5)

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