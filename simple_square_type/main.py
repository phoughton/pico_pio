import time
import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1) [10]
    set(pins, 0) [5]
    set(pins, 1) [20]
    set(pins, 0) [5]
    wrap()

sm = rp2.StateMachine(0, blink, freq=20000, set_base=Pin(0))

sm.active(1)
