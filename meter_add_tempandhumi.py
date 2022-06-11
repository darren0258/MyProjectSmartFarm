import lvgl as lv
import dht

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
a1.set_values(0, 1)
a1.set_time(2000)
a1.set_repeat_delay(100)
a1.set_var(indic1)
a1.set_custom_exec_cb(lambda a,val: set_value(indic1,val))
lv.anim_t.start(a1)

a2 = lv.anim_t()
a2.init()
a2.set_values(0, 1)
a2.set_time(1000)
a2.set_repeat_delay(100)
a2.set_var(indic2)
a2.set_custom_exec_cb(lambda a,val: set_value(indic2,val))
lv.anim_t.start(a2)

sensor = dht.DHT22(Pin(25))

temp_style = lv.style_t()
spans_group = lv.spangroup(lv.scr_act())
span_temp = spans_group.new_span()
span_temp.style.set_text_color(lv.palette_main(lv.PALETTE.BLUE))
spans_group.align(lv.ALIGN.TOP_RIGHT, 0, 0)

humi_style = lv.style_t()
spans_group2 = lv.spangroup(lv.scr_act())
span_humi = spans_group2.new_span()
span_humi.style.set_text_color(lv.palette_main(lv.PALETTE.GREEN))
spans_group2.align(lv.ALIGN.TOP_RIGHT, 0, 20)


def mycallback(t):
    sensor.measure()
    temp = sensor.temperature()
    humi = sensor.humidity()
    a1.set_values(int(temp), int(temp))
    a2.set_values(int(humi), int(humi))
    lv.anim_t.start(a1)
    lv.anim_t.start(a2)
    
    span_temp.set_text_static("temp : " + str(int(temp)))
    span_humi.set_text_static("humi : " + str(int(humi)))
    
tim = machine.Timer(1)
tim.init(period=1000, callback=mycallback)



