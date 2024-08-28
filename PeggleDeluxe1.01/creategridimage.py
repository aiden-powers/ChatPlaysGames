import PIL
import PIL.Image

from dimensionhelper import dimensionsClass

dims = dimensionsClass()

def create_grid_image():
    # peggle window must exist in desktop to do this
    grid_image = PIL.Image.new("RGB", (dims.width, dims.height), "white")
    for i in range(11):
        x = int((dims.width / 10) * i)
        y = int((dims.height / 10) * i)
        if 0 <= x < dims.width:
            for j in range(dims.height):
                grid_image.putpixel((x, j), (0, 0, 0))
        if 0 <= y < dims.height:
            for j in range(dims.width):
                grid_image.putpixel((j, y), (0, 0, 0))
    grid_image.show()

create_grid_image()