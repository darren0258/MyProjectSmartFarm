import lvgl as lv
import machine, dht
from imagetools import get_png_info, open_png
import dht
from machine import Pin, Timer
from time import sleep
import lodepng as png


from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)

from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)

tabview = lv.tabview(lv.scr_act(), lv.DIR.LEFT, 80)
tabview.set_style_bg_color(lv.palette_lighten(lv.PALETTE.BLUE_GREY, 2), 0)

tab_btns = tabview.get_tab_btns()
tab_btns.set_style_bg_color(lv.palette_darken(lv.PALETTE.GREY, 3), 0)
tab_btns.set_style_text_color(lv.palette_lighten(lv.PALETTE.GREY, 5), 0)
tab_btns.set_style_border_side(lv.BORDER_SIDE.RIGHT, lv.PART.ITEMS | lv.STATE.CHECKED)

tab1 = tabview.add_tab("Tab 1")
tab2 = tabview.add_tab("Tab 2")
tab3 = tabview.add_tab("Tab 3")



def set_value(indic,v):
    meter.set_indicator_end_value(indic, v)   

meter = lv.meter(tab1)
meter.align(lv.ALIGN.CENTER, 0, 20)
meter.set_size(190, 190)

meter.remove_style(None, lv.PART.INDICATOR)

scale = meter.add_scale()
meter.set_scale_ticks(scale, 11, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale, 1, 2, 25, lv.color_hex3(0xeee), 10)
meter.set_scale_range(scale, 0, 100, 270, 90)

indic1 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.BLUE), 0)
indic2 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.LIME), -10)

a1 = lv.anim_t()
a1.init()
a1.set_values(0, 1)
a1.set_time(2000)
a1.set_var(indic1)
a1.set_custom_exec_cb(lambda a,val: set_value(indic1,val))

a2 = lv.anim_t()
a2.init()
a2.set_values(0, 1)
a2.set_time(1000)
a2.set_var(indic2)
a2.set_custom_exec_cb(lambda a,val: set_value(indic2,val))


sensor = dht.DHT22(Pin(25))

def mycallback(t):
    sensor.measure()
    temp = sensor.temperature()
    humi = sensor.humidity()
    a1.set_values(int(temp), int(temp))
    a2.set_values(int(humi), int(humi))
    lv.anim_t.start(a1)
    lv.anim_t.start(a2)
    
tim = machine.Timer(1)
tim.init(period=1000, callback=mycallback)




