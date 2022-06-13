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
labeltab1.set_text("Tab 1")
labeltab1.align(lv.ALIGN.CENTER, 0, 0)

labeltab2 = lv.label(tab2)
labeltab2.set_text("Tab 2")
labeltab2.align(lv.ALIGN.CENTER, 0, 0)

labeltab3 = lv.label(tab3)
labeltab3.set_text("Tab 3")
labeltab3.align(lv.ALIGN.CENTER, 0, 0)






# Define the function of each switch.
def event_handlerR1(e):
    r1code = e.get_code()
    r1obj = e.get_target()
    if r1code == lv.EVENT.VALUE_CHANGED:
        if r1obj.has_state(lv.STATE.CHECKED):
            relay12.value(1)
        else:
            relay12.value(0)
            
def event_handlerR2(e):
    r2code = e.get_code()
    r2obj = e.get_target()
    if r2code == lv.EVENT.VALUE_CHANGED:
        if r2obj.has_state(lv.STATE.CHECKED):
            relay13.value(1)
        else:
            relay13.value(0)
            
def event_handlerR3(e):
    r3code = e.get_code()
    r3obj = e.get_target()
    if r3code == lv.EVENT.VALUE_CHANGED:
        if r3obj.has_state(lv.STATE.CHECKED):
            relay14.value(1)
        else:
            relay14.value(0)
            
def event_handlerR4(e):
    r4code = e.get_code()
    r4obj = e.get_target()
    if r4code == lv.EVENT.VALUE_CHANGED:
        if r4obj.has_state(lv.STATE.CHECKED):
            relay15.value(1)
        else:
            relay15.value(0)

# Used for alignment and positioning in the screen.
tab1.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
tab1.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)



sw1 = lv.switch(tab1)
sw1.add_event_cb(event_handlerR1 ,lv.EVENT.ALL, None)






