import lvgl as lv
import lodepng as png
from imagetools import get_png_info, open_png


decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png
with open('kku9.png' ,'rb') as f: # Read the pictures that we have brought into the board.
      png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data})

img1 = lv.img(lv.scr_act())
img1.center()
img1.set_src(png_img_dsc)


