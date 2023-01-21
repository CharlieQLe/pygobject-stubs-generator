from gi.repository import GdkPixbuf, GdkPixbuf, GObject

PIXBUF_MAGIC_NUMBER: int
PIXDATA_HEADER_LENGTH: int

def pixbuf_from_pixdata(pixdata: Pixdata, copy_pixels: bool) -> GdkPixbuf.Pixbuf: ...

class PixdataDumpType(GObject.GFlag): 
    PIXDATA_STREAM = ...
    PIXDATA_STRUCT = ...
    MACROS = ...
    GTYPES = ...
    CTYPES = ...
    STATIC = ...
    CONST = ...
    RLE_DECODER = ...

class PixdataType(GObject.GFlag): 
    COLOR_TYPE_RGB = ...
    COLOR_TYPE_RGBA = ...
    COLOR_TYPE_MASK = ...
    SAMPLE_WIDTH_8 = ...
    SAMPLE_WIDTH_MASK = ...
    ENCODING_RAW = ...
    ENCODING_RLE = ...
    ENCODING_MASK = ...
