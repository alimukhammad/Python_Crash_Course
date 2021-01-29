import io
from barcode import EAN13
from barcode.write import ImageWriter
from PIL import Image

def bar_generator(digits=123456789123):
    #digits is the defaultvalue
    #io.BytesIO makes sure you only save to memory instead of disk
    rv = io.BytesIO()
    EAN13(str(digits), write=ImageWriter()).write(rv)
    image = Image.open(rv)
    #resize and display the bar code
    image = image.resize((400,400), Image.ANTIALIAS)
    image.show()

if __name__=="__main__":
    bar_generator()