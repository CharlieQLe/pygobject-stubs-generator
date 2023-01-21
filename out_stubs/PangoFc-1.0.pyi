from gi.repository import fontconfig, Pango, freetype2, GLib, HarfBuzz, Pango, fontconfig

FONT_FEATURES: str
FONT_VARIATIONS: str
GRAVITY: str
PRGNAME: str
VERSION: str


class Decoder(GObject.Object): 
    def get_charset(self, fcfont: Font) -> fontconfig.CharSet: ...
    def get_glyph(self, fcfont: Font, wc: int) -> Pango.Glyph: ...

class Font(Pango.Font): 
    @classmethod
    def description_from_pattern(cls, pattern: fontconfig.Pattern, include_size: bool) -> Pango.FontDescription: ...
    def get_glyph(self, wc: gunichar) -> int: ...
    def get_languages(self) -> list[Pango.Language]: ...
    def get_pattern(self) -> fontconfig.Pattern: ...
    def get_unknown_glyph(self, wc: gunichar) -> Pango.Glyph: ...
    def has_char(self, wc: gunichar) -> bool: ...
    def kern_glyphs(self, glyphs: Pango.GlyphString) -> None: ...
    def lock_face(self) -> freetype2.Face: ...
    def unlock_face(self) -> None: ...

class FontMap(Pango.FontMap, Gio.ListModel): 
    def add_decoder_find_func(self, findfunc: DecoderFindFunc, user_data: object, dnotify: GLib.DestroyNotify) -> None: ...
    def cache_clear(self) -> None: ...
    def config_changed(self) -> None: ...
    def create_context(self) -> Pango.Context: ...
    def find_decoder(self, pattern: fontconfig.Pattern) -> Decoder: ...
    def get_config(self) -> fontconfig.Config: ...
    def get_hb_face(self, fcfont: Font) -> HarfBuzz.face_t: ...
    def set_config(self, fcconfig: fontconfig.Config) -> None: ...
    def set_default_substitute(self, func: SubstituteFunc, data: object, notify: GLib.DestroyNotify) -> None: ...
    def shutdown(self) -> None: ...
    def substitute_changed(self) -> None: ...
