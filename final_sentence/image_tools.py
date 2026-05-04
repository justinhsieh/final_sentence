"""Image helpers used by the Tkinter UI."""

from PIL import Image, ImageDraw, ImageFont, ImageTk


def create_rotated_text_image(text, font_size, color, angle, font_file="courbd.ttf"):
    # Create rotated text as a Tk image.
    try:
        font = ImageFont.truetype(font_file, font_size)
    except IOError:
        try:
            font = ImageFont.truetype("timesbd.ttf", font_size)
        except IOError:
            try:
                font = ImageFont.truetype("Courier New Bold.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()
    dummy_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bbox = dummy_draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    canvas_size = int(max(text_width, text_height) * 1.5)
    img = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((canvas_size / 2, canvas_size / 2), text, font=font, fill=color, anchor="mm")
    rotated_img = img.rotate(angle, resample=Image.BICUBIC, expand=True)
    return ImageTk.PhotoImage(rotated_img)

