import lvgl as lv
import lodepng as png
from imagetools import get_png_info, open_png

from ili9XXX import ili9341
disp = ili9341(spihost=1,mosi=23,miso=19,clk=18,cs=5,dc=21,rst=22, rot=0x20,width=320, height=240)

from xpt2046 import xpt2046
touch = xpt2046(cs=33,mhz=1,transpose=False, cal_x0=3780, cal_y1=252, cal_x1=393, cal_y0=3751)

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png
with open('kku9.png' ,'rb') as f:
      png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data})

img1 = lv.img(lv.scr_act())
img1.center()
img1.set_src(png_img_dsc)


