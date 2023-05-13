#!/usr/bin/env python

import sys
import time

import scrollphat

brightness = scrollphat.set_brightness(5)

while True:
    try:
        scrollphat.write_string(time.strftime("%H:%M     "))
        scrollphat.scroll(1)
        time.sleep(0.5)

    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

