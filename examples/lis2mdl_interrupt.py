# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_lis2mdl

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
lis = adafruit_lis2mdl.LIS2MDL(i2c)
lis.interrupt_threshold = 80
lis.interrupt_enabled = True

while True:
    x_hi, y_hi, z_hi, x_lo, y_lo, z_lo, int_triggered = lis.faults

    print(lis.magnetic)
    print(f"Xhi:{x_hi}\tYhi:{y_hi}\tZhi:{z_hi}")
    print(f"Xlo:{x_lo}\tYlo:{y_lo}\tZlo:{z_lo}")
    print(f"Int triggered: {int_triggered}")
    print()

    time.sleep(1)
