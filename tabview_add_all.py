import lvgl as lv

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

tab1.set_style_bg_color(lv.palette_lighten(lv.PALETTE.DEEP_ORANGE, 3), 0)
tab1.set_style_bg_opa(lv.OPA.COVER, 0)

tab2.set_style_bg_color(lv.palette_lighten(lv.PALETTE.AMBER, 3), 0)
tab2.set_style_bg_opa(lv.OPA.COVER, 0)

tab3.set_style_bg_color(lv.palette_lighten(lv.PALETTE.RED, 1), 0)
tab3.set_style_bg_opa(lv.OPA.COVER, 0)

labeltab1 = lv.label(tab1)
labeltab2.set_text("Tab 1")
labeltab3.align(lv.ALIGN.CENTER, 0, 0)

labeltab2 = lv.label(tab2)
labeltab2.set_text("Tab 2")
labeltab2.align(lv.ALIGN.CENTER, 0, 0)

labeltab3 = lv.label(tab3)
labeltab3.set_text("Tab 3")
labeltab3.align(lv.ALIGN.CENTER, 0, 0)


def event_handlerR1(e):
    r1code = e.get_code()
    r1obj = e.get_target()
    if r1code == lv.EVENT.VALUE_CHANGED:
        print("aa")
        
def event_handlerR2(e):
    r1code = e.get_code()
    r1obj = e.get_target()
    if r1code == lv.EVENT.VALUE_CHANGED:
        print("aa")

tab1.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
tab1.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)


sw1 = lv.switch(tab1)
sw1.add_event_cb(event_handlerR1 ,lv.EVENT.ALL, None)

sw2 = lv.switch(tab1)
sw2.add_event_cb(event_handlerR2 ,lv.EVENT.ALL, None)


decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png
with open('kku9.png' ,'rb') as f:
      png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data})

img1 = lv.img(tab2)
img1.center()
img1.set_src(png_img_dsc)






def set_value(indic,v):
    meter.set_indicator_end_value(indic, v)   

    
#
# A meter with multiple arcs.
#

meter = lv.meter(tab3)
meter.align(lv.ALIGN.CENTER, 0, 20)
meter.set_size(190, 190)

# Remove the circle from the middle.
meter.remove_style(None, lv.PART.INDICATOR)

# Add a scale first.
scale = meter.add_scale()
meter.set_scale_ticks(scale, 11, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale, 1, 2, 25, lv.color_hex3(0xeee), 10)
meter.set_scale_range(scale, 0, 100, 270, 90)

# Add a three arc indicator.
indic1 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.BLUE), 0)
indic2 = meter.add_arc(scale, 10, lv.palette_main(lv.PALETTE.LIME), -10)

# Create an animation to set the value.
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
    


# periodic with 1000ms period.
tim = machine.Timer(1)
tim.init(period=1000, callback=mycallback)



