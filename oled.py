import Adafruit_SSD1306
from PIL import ImageFont, Image, ImageDraw

disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
font = ImageFont.load_default()


def update_disp(text):
	global disp, width, height, font

	img = Image.new('1', (width, height))
	draw = ImageDraw.Draw(img)
	draw.text((0, 14), text, font=font, fill=255)
	disp.image(img)
	disp.display()
