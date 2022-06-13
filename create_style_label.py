import lvgl as lv

from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)

from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)

style = lv.style_t()
style.init()

style.set_border_width(5)
style.set_border_color(lv.palette_main(lv.PALETTE.RED))
style.set_pad_all(10)

style.set_text_color(lv.palette_main(lv.PALETTE.BLUE))
style.set_text_letter_space(5)
style.set_text_decor(lv.TEXT_DECOR.UNDERLINE)

label = lv.label(lv.scr_act())
label.set_text("Style")
label.align(lv.ALIGN.CENTER, 0, 0)
label.add_style(style, 0)