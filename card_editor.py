from PIL import Image

class CardEditor():
    @staticmethod
    def add_border(image_path):
        #topleft = 11,11
        #bottomright = 723, 1001
        im = Image.open(image_path)
        im_crop = im.crop((11, 11, 723, 1001))
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((1, 350))

        im_w, im_h = im_crop.size
        bg_im = Image.new('RGB', (int(im_w*1.05), int(im_h*1.05)), (r, g, b))
        bg_w, bg_h = bg_im.size
        offset = ((bg_w - im_w) // 2, (bg_h - im_h) // 2)
        bg_im.paste(im_crop, offset)
        bg_im.save(image_path)
        
    
    @staticmethod
    def fix_dpi(image_path):
        im = Image.open(image_path)
        im.save(image_path, dpi=(600, 600))
    