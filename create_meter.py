import lvgl as lv

from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)

from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)


def set_value(indic,v):
    meter.set_indicator_end_value(indic, v)   

meter = lv.meter(lv.scr_act())
meter.align(lv.ALIGN.CENTER, 0, 20)
meter.set_size(190, 190)

meter.remove_style(None, lv.PART.INDICATOR)

scale = meter.add_scale()
meter.set_scale_ticks(scale, 11, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale, 1, 2, 30, lv.color_hex3(0xeee), 10)
meter.set_scale_range(scale, 0, 100, 270, 90)

indic1 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.BLUE), 0)
indic2 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.LIME), -10)

a1 = lv.anim_t()
a1.init()
a1.set_values(0, 100)
a1.set_time(2000)
a1.set_repeat_delay(100)
a1.set_var(indic1)
a1.set_custom_exec_cb(lambda a,val: set_value(indic1,val))
lv.anim_t.start(a1)

a2 = lv.anim_t()
a2.init()
a2.set_values(0, 70)
a2.set_time(1000)
a2.set_repeat_delay(100)
a2.set_var(indic2)
a2.set_custom_exec_cb(lambda a,val: set_value(indic2,val))
lv.anim_t.start(a2)


