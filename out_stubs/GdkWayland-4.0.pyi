from gi.repository import GLib, Gdk


class WaylandDevice(Gdk.Device): 
    def get_node_path(self) -> str: ...
    def get_wl_keyboard(self) -> object: ...
    def get_wl_pointer(self) -> object: ...
    def get_wl_seat(self) -> object: ...
    def get_xkb_keymap(self) -> object: ...

class WaylandDisplay(Gdk.Display): 
    def get_egl_display(self) -> object: ...
    def get_startup_notification_id(self) -> str: ...
    def get_wl_compositor(self) -> object: ...
    def get_wl_display(self) -> object: ...
    def query_registry(self, global: str) -> bool: ...
    def set_cursor_theme(self, name: str, size: int) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...

class WaylandGLContext(Gdk.GLContext): ...

class WaylandMonitor(Gdk.Monitor): 
    def get_wl_output(self) -> object: ...

class WaylandPopup(WaylandSurface, Gdk.Popup): ...

class WaylandSeat(Gdk.Seat): 
    def get_wl_seat(self) -> object: ...

class WaylandSurface(Gdk.Surface): 
    def get_wl_surface(self) -> object: ...

class WaylandToplevel(WaylandSurface, Gdk.Toplevel): 
    def export_handle(self, callback: WaylandToplevelExported, user_data: object, destroy_func: GLib.DestroyNotify) -> bool: ...
    def set_application_id(self, application_id: str) -> None: ...
    def set_transient_for_exported(self, parent_handle_str: str) -> bool: ...
    def unexport_handle(self) -> None: ...

