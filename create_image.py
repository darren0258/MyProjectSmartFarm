import lvgl as lv
from imagetools import get_png_info, open_png

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

with open('../../assets/img_cogwheel_argb.png','rb') as f:
    png_data = f.read()

img_cogwheel_argb = lv.img_dsc_t({
  'data_size': len(png_data),
  'data': png_data
})


img = lv.img(lv.scr_act())
img.set_src(img_cogwheel_argb)
img.align(lv.ALIGN.CENTER, 0, 0)


