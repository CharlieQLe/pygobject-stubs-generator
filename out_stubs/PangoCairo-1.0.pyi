from gi.repository import Pango, cairo, GLib, GObject, Pango, cairo

def context_get_font_options(context: Pango.Context) -> cairo.FontOptions: ...
def context_get_resolution(context: Pango.Context) -> float: ...
def context_get_shape_renderer(context: Pango.Context, data: object) -> ShapeRendererFunc: ...
def context_set_font_options(context: Pango.Context, options: cairo.FontOptions) -> None: ...
def context_set_resolution(context: Pango.Context, dpi: float) -> None: ...
def context_set_shape_renderer(context: Pango.Context, func: ShapeRendererFunc, data: object, dnotify: GLib.DestroyNotify) -> None: ...
def create_context(cr: cairo.Context) -> Pango.Context: ...
def create_layout(cr: cairo.Context) -> Pango.Layout: ...
def error_underline_path(cr: cairo.Context, x: float, y: float, width: float, height: float) -> None: ...
def font_map_get_default() -> Pango.FontMap: ...
def font_map_new() -> Pango.FontMap: ...
def font_map_new_for_font_type(fonttype: cairo.FontType) -> Pango.FontMap: ...
def glyph_string_path(cr: cairo.Context, font: Pango.Font, glyphs: Pango.GlyphString) -> None: ...
def layout_line_path(cr: cairo.Context, line: Pango.LayoutLine) -> None: ...
def layout_path(cr: cairo.Context, layout: Pango.Layout) -> None: ...
def show_error_underline(cr: cairo.Context, x: float, y: float, width: float, height: float) -> None: ...
def show_glyph_item(cr: cairo.Context, text: str, glyph_item: Pango.GlyphItem) -> None: ...
def show_glyph_string(cr: cairo.Context, font: Pango.Font, glyphs: Pango.GlyphString) -> None: ...
def show_layout(cr: cairo.Context, layout: Pango.Layout) -> None: ...
def show_layout_line(cr: cairo.Context, line: Pango.LayoutLine) -> None: ...
def update_context(cr: cairo.Context, context: Pango.Context) -> None: ...
def update_layout(cr: cairo.Context, layout: Pango.Layout) -> None: ...

class Font(Pango.Font): 
    def get_scaled_font(self) -> cairo.ScaledFont: ...
class FontMap(Pango.FontMap): 
    def create_context(self) -> Pango.Context: ...
    def get_font_type(self) -> cairo.FontType: ...
    def get_resolution(self) -> float: ...
    def set_default(self) -> None: ...
    def set_resolution(self, dpi: float) -> None: ...

