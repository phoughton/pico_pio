import time
import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW, out_init=rp2.PIO.OUT_LOW,
             autopull=True, out_shiftdir=rp2.PIO.SHIFT_RIGHT, pull_thresh=8,
              sideset_init=(rp2.PIO.OUT_LOW, rp2.PIO.OUT_HIGH))
def write_num():
    wrap_target()
    pull()
    out(pins,1) .side(1) [1]  
    out(pins,1) .side(0) [1]  

    out(pins,1) .side(1) [1]  
    out(pins,1) .side(0) [1]
    
    out(pins,1) .side(1) [1]  
    out(pins,1) .side(0) [1]
    
    out(pins,1) .side(1) [1]  
    out(pins,1) .side(0) [1]
    
    set(pins, 0) [3]
    #nop() [8]
    wrap()

sm = rp2.StateMachine(0, write_num, freq=20000, set_base=Pin(0), out_base=Pin(0), sideset_base=Pin(15))

sm.active(1)

#while True:
#sm.put("a")
#sm.put("b")
sm.put("c")
sm.put("O")

#sm.put("d")