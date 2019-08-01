


def get_valid_img(request):
    import random
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    from PIL import Image
    from io import BytesIO
    from PIL import ImageDraw, ImageFont
    f = BytesIO()

    image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("app01/static/font/kumo.ttf", size=36)

    temp = []
    for i in range(5):
        random_char = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        draw.text((i * 24, 26), random_char, get_random_color(), font=font)
        temp.append(random_char)

    width = 120
    height = 80

    # for i in range(80):
    #     draw.point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())
    #
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    # for i in range(40):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    image.save(f, "png")
    data = f.getvalue()


    return data,temp

