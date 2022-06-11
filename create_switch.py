import lvgl as lv

from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)

from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)


def event_handlerR1(e):
    r1code = e.get_code()
    r1obj = e.get_target()
    if r1code == lv.EVENT.VALUE_CHANGED:
        print("aa")

sw = lv.switch(lv.scr_act())
sw.align(lv.ALIGN.CENTER, 0, 0)
sw.add_event_cb(event_handlerR1 ,lv.EVENT.ALL, None)



