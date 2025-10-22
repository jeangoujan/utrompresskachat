from PIL import Image, ImageDraw, ImageFont
import io


def create_meme(morning_tasks, evening_tasks):
    img = Image.open('static/template.jpg').convert('RGB')
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('fonts/UtromPressKachat.ttf', size=233)


    morning_coords = [
        (510, 530),   # 1.
        (810, 780),   # 2.
        (510, 1050),   # 3.
        (510, 1320)    # 4.
    ]


    evening_coords = [
        (510, 1850),   # 1.
        (510, 2100),  # 2.
        (510, 2380),  # 3.
        (510, 2630),  # 4.
        (510, 2880)   # 5.
    ]


    fill_color = 'black'


    for i, text in enumerate(morning_tasks[:4]):
        x, y = morning_coords[i]
        draw.text((x, y), text, fill=fill_color, font=font)


    for i, text in enumerate(evening_tasks[:5]):
        x, y = evening_coords[i]
        draw.text((x, y), text, fill=fill_color, font=font)


    output = io.BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)
    return output.getvalue()