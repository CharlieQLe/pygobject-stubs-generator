from gi.repository import GObject, GObject

BINARY_AGE: int
INTERFACE_AGE: int
MAJOR_VERSION: int
MICRO_VERSION: int
MINOR_VERSION: int
VERSION_MIN_REQUIRED: int

def add_focus_tracker(focus_tracker: EventListener) -> int: ...
def add_global_event_listener(listener: GObject.SignalEmissionHook, event_type: str) -> int: ...
def add_key_event_listener(listener: KeySnoopFunc, data: object) -> int: ...
def attribute_set_free(attrib_set: AttributeSet) -> None: ...
def focus_tracker_init(init: EventListenerInit) -> None: ...
def focus_tracker_notify(object: Object) -> None: ...
def get_binary_age() -> int: ...
def get_default_registry() -> Registry: ...
def get_focus_object() -> Object: ...
def get_interface_age() -> int: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_root() -> Object: ...
def get_toolkit_name() -> str: ...
def get_toolkit_version() -> str: ...
def get_version() -> str: ...
def relation_type_for_name(name: str) -> RelationType: ...
def relation_type_get_name(type: RelationType) -> str: ...
def relation_type_register(name: str) -> RelationType: ...
def remove_focus_tracker(tracker_id: int) -> None: ...
def remove_global_event_listener(listener_id: int) -> None: ...
def remove_key_event_listener(listener_id: int) -> None: ...
def role_for_name(name: str) -> Role: ...
def role_get_localized_name(role: Role) -> str: ...
def role_get_name(role: Role) -> str: ...
def role_register(name: str) -> Role: ...
def state_type_for_name(name: str) -> StateType: ...
def state_type_get_name(type: StateType) -> str: ...
def state_type_register(name: str) -> StateType: ...
def text_attribute_for_name(name: str) -> TextAttribute: ...
def text_attribute_get_name(attr: TextAttribute) -> str: ...
def text_attribute_get_value(attr: TextAttribute, index_: int) -> str: ...
def text_attribute_register(name: str) -> TextAttribute: ...
def text_free_ranges(ranges: list[TextRange]) -> None: ...
def value_type_get_localized_name(value_type: ValueType) -> str: ...
def value_type_get_name(value_type: ValueType) -> str: ...

class GObjectAccessible(Object): 
    @classmethod
    def for_object(cls, obj: GObject.Object) -> Object: ...
    def get_object(self) -> GObject.Object: ...

class Hyperlink(GObject.Object, Action): 
    def get_end_index(self) -> int: ...
    def get_n_anchors(self) -> int: ...
    def get_object(self, i: int) -> Object: ...
    def get_start_index(self) -> int: ...
    def get_uri(self, i: int) -> str: ...
    def is_inline(self) -> bool: ...
    def is_selected_link(self) -> bool: ...
    def is_valid(self) -> bool: ...

class Misc(GObject.Object): 
    @classmethod
    def get_instance(cls) -> Misc: ...
    def threads_enter(self) -> None: ...
    def threads_leave(self) -> None: ...

class NoOpObject(Object, Action, Component, Document, EditableText, Hypertext, Image, Selection, Table, TableCell, Text, Value, Window): 
    @classmethod
    def new(cls, obj: GObject.Object) -> Object: ...

class NoOpObjectFactory(ObjectFactory): 
    @classmethod
    def new(cls) -> ObjectFactory: ...

class Object(GObject.Object): 
    def add_relationship(self, relationship: RelationType, target: Object) -> bool: ...
    def connect_property_change_handler(self, handler: PropertyChangeHandler) -> int: ...
    def get_accessible_id(self) -> str: ...
    def get_attributes(self) -> AttributeSet: ...
    def get_description(self) -> str: ...
    def get_index_in_parent(self) -> int: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    def get_n_accessible_children(self) -> int: ...
    def get_name(self) -> str: ...
    def get_object_locale(self) -> str: ...
    def get_parent(self) -> Object: ...
    def get_role(self) -> Role: ...
    def initialize(self, data: object) -> None: ...
    def notify_state_change(self, state: State, value: bool) -> None: ...
    def peek_parent(self) -> Object: ...
    def ref_accessible_child(self, i: int) -> Object: ...
    def ref_relation_set(self) -> RelationSet: ...
    def ref_state_set(self) -> StateSet: ...
    def remove_property_change_handler(self, handler_id: int) -> None: ...
    def remove_relationship(self, relationship: RelationType, target: Object) -> bool: ...
    def set_accessible_id(self, name: str) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_parent(self, parent: Object) -> None: ...
    def set_role(self, role: Role) -> None: ...

class ObjectFactory(GObject.Object): 
    def create_accessible(self, obj: GObject.Object) -> Object: ...
    def get_accessible_type(self) -> GObject.Type: ...
    def invalidate(self) -> None: ...

class Plug(Object, Component): 
    @classmethod
    def new(cls) -> Object: ...
    def get_id(self) -> str: ...
    def set_child(self, child: Object) -> None: ...

class Registry(GObject.Object): 
    def get_factory(self, type: GObject.Type) -> ObjectFactory: ...
    def get_factory_type(self, type: GObject.Type) -> GObject.Type: ...
    def set_factory_type(self, type: GObject.Type, factory_type: GObject.Type) -> None: ...

class Relation(GObject.Object): 
    @classmethod
    def new(cls, targets: list[Object], n_targets: int, relationship: RelationType) -> Relation: ...
    def add_target(self, target: Object) -> None: ...
    def get_relation_type(self) -> RelationType: ...
    def get_target(self) -> list[Object]: ...
    def remove_target(self, target: Object) -> bool: ...

class RelationSet(GObject.Object): 
    @classmethod
    def new(cls) -> RelationSet: ...
    def add(self, relation: Relation) -> None: ...
    def add_relation_by_type(self, relationship: RelationType, target: Object) -> None: ...
    def contains(self, relationship: RelationType) -> bool: ...
    def contains_target(self, relationship: RelationType, target: Object) -> bool: ...
    def get_n_relations(self) -> int: ...
    def get_relation(self, i: int) -> Relation: ...
    def get_relation_by_type(self, relationship: RelationType) -> Relation: ...
    def remove(self, relation: Relation) -> None: ...

class Socket(Object, Component): 
    @classmethod
    def new(cls) -> Object: ...
    def embed(self, plug_id: str) -> None: ...
    def is_occupied(self) -> bool: ...

class StateSet(GObject.Object): 
    @classmethod
    def new(cls) -> StateSet: ...
    def add_state(self, type: StateType) -> bool: ...
    def add_states(self, types: list[StateType], n_types: int) -> None: ...
    def and_sets(self, compare_set: StateSet) -> StateSet: ...
    def clear_states(self) -> None: ...
    def contains_state(self, type: StateType) -> bool: ...
    def contains_states(self, types: list[StateType], n_types: int) -> bool: ...
    def is_empty(self) -> bool: ...
    def or_sets(self, compare_set: StateSet) -> StateSet: ...
    def remove_state(self, type: StateType) -> bool: ...
    def xor_sets(self, compare_set: StateSet) -> StateSet: ...

class Util(GObject.Object): ...

class Action: 
    def do_action(self, i: int) -> bool: ...
    def get_description(self, i: int) -> str: ...
    def get_keybinding(self, i: int) -> str: ...
    def get_localized_name(self, i: int) -> str: ...
    def get_n_actions(self) -> int: ...
    def get_name(self, i: int) -> str: ...
    def set_description(self, i: int, desc: str) -> bool: ...
    def do_action(self, i: int) -> bool: ...
    def get_description(self, i: int) -> str: ...
    def get_keybinding(self, i: int) -> str: ...
    def get_localized_name(self, i: int) -> str: ...
    def get_n_actions(self) -> int: ...
    def get_name(self, i: int) -> str: ...
    def set_description(self, i: int, desc: str) -> bool: ...
class Component: 
    def add_focus_handler(self, handler: FocusHandler) -> int: ...
    def bounds_changed(self, bounds: Rectangle) -> None: ...
    def contains(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, x: int, y: int, width: int, height: int, coord_type: CoordType) -> None: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    def get_position(self, x: int, y: int, coord_type: CoordType) -> None: ...
    def get_size(self, width: int, height: int) -> None: ...
    def grab_focus(self) -> bool: ...
    def ref_accessible_at_point(self, x: int, y: int, coord_type: CoordType) -> Object: ...
    def remove_focus_handler(self, handler_id: int) -> None: ...
    def scroll_to(self, type: ScrollType) -> bool: ...
    def scroll_to_point(self, coords: CoordType, x: int, y: int) -> bool: ...
    def set_extents(self, x: int, y: int, width: int, height: int, coord_type: CoordType) -> bool: ...
    def set_position(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...
    def add_focus_handler(self, handler: FocusHandler) -> int: ...
    def contains(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, x: int, y: int, width: int, height: int, coord_type: CoordType) -> None: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    def get_position(self, x: int, y: int, coord_type: CoordType) -> None: ...
    def get_size(self, width: int, height: int) -> None: ...
    def grab_focus(self) -> bool: ...
    def ref_accessible_at_point(self, x: int, y: int, coord_type: CoordType) -> Object: ...
    def remove_focus_handler(self, handler_id: int) -> None: ...
    def scroll_to(self, type: ScrollType) -> bool: ...
    def scroll_to_point(self, coords: CoordType, x: int, y: int) -> bool: ...
    def set_extents(self, x: int, y: int, width: int, height: int, coord_type: CoordType) -> bool: ...
    def set_position(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...
class Document: 
    def get_current_page_number(self) -> int: ...
    def get_document(self) -> object: ...
    def get_document_attribute_value(self, attribute_name: str) -> str: ...
    def get_document_attributes(self) -> AttributeSet: ...
    def get_document_locale(self) -> str: ...
    def get_document_type(self) -> str: ...
    def get_page_count(self) -> int: ...
    def set_document_attribute(self, attribute_name: str, attribute_value: str) -> bool: ...
    def get_attribute_value(self, attribute_name: str) -> str: ...
    def get_attributes(self) -> AttributeSet: ...
    def get_current_page_number(self) -> int: ...
    def get_document(self) -> object: ...
    def get_document_type(self) -> str: ...
    def get_locale(self) -> str: ...
    def get_page_count(self) -> int: ...
    def set_attribute_value(self, attribute_name: str, attribute_value: str) -> bool: ...
class EditableText: 
    def copy_text(self, start_pos: int, end_pos: int) -> None: ...
    def cut_text(self, start_pos: int, end_pos: int) -> None: ...
    def delete_text(self, start_pos: int, end_pos: int) -> None: ...
    def insert_text(self, string: str, length: int, position: int) -> None: ...
    def paste_text(self, position: int) -> None: ...
    def set_run_attributes(self, attrib_set: AttributeSet, start_offset: int, end_offset: int) -> bool: ...
    def set_text_contents(self, string: str) -> None: ...
    def copy_text(self, start_pos: int, end_pos: int) -> None: ...
    def cut_text(self, start_pos: int, end_pos: int) -> None: ...
    def delete_text(self, start_pos: int, end_pos: int) -> None: ...
    def insert_text(self, string: str, length: int, position: int) -> None: ...
    def paste_text(self, position: int) -> None: ...
    def set_run_attributes(self, attrib_set: AttributeSet, start_offset: int, end_offset: int) -> bool: ...
    def set_text_contents(self, string: str) -> None: ...
class HyperlinkImpl: 
    def get_hyperlink(self) -> Hyperlink: ...
    def get_hyperlink(self) -> Hyperlink: ...
class Hypertext: 
    def get_link(self, link_index: int) -> Hyperlink: ...
    def get_link_index(self, char_index: int) -> int: ...
    def get_n_links(self) -> int: ...
    def link_selected(self, link_index: int) -> None: ...
    def get_link(self, link_index: int) -> Hyperlink: ...
    def get_link_index(self, char_index: int) -> int: ...
    def get_n_links(self) -> int: ...
class Image: 
    def get_image_description(self) -> str: ...
    def get_image_locale(self) -> str: ...
    def get_image_position(self, x: int, y: int, coord_type: CoordType) -> None: ...
    def get_image_size(self, width: int, height: int) -> None: ...
    def set_image_description(self, description: str) -> bool: ...
    def get_image_description(self) -> str: ...
    def get_image_locale(self) -> str: ...
    def get_image_position(self, x: int, y: int, coord_type: CoordType) -> None: ...
    def get_image_size(self, width: int, height: int) -> None: ...
    def set_image_description(self, description: str) -> bool: ...
class ImplementorIface: ...
class Selection: 
    def add_selection(self, i: int) -> bool: ...
    def clear_selection(self) -> bool: ...
    def get_selection_count(self) -> int: ...
    def is_child_selected(self, i: int) -> bool: ...
    def ref_selection(self, i: int) -> Object: ...
    def remove_selection(self, i: int) -> bool: ...
    def select_all_selection(self) -> bool: ...
    def selection_changed(self) -> None: ...
    def add_selection(self, i: int) -> bool: ...
    def clear_selection(self) -> bool: ...
    def get_selection_count(self) -> int: ...
    def is_child_selected(self, i: int) -> bool: ...
    def ref_selection(self, i: int) -> Object: ...
    def remove_selection(self, i: int) -> bool: ...
    def select_all_selection(self) -> bool: ...
class StreamableContent: 
    def get_mime_type(self, i: int) -> str: ...
    def get_n_mime_types(self) -> int: ...
    def get_stream(self, mime_type: str) -> GLib.IOChannel: ...
    def get_uri(self, mime_type: str) -> str: ...
    def get_mime_type(self, i: int) -> str: ...
    def get_n_mime_types(self) -> int: ...
    def get_stream(self, mime_type: str) -> GLib.IOChannel: ...
    def get_uri(self, mime_type: str) -> str: ...
class Table: 
    def add_column_selection(self, column: int) -> bool: ...
    def add_row_selection(self, row: int) -> bool: ...
    def column_deleted(self, column: int, num_deleted: int) -> None: ...
    def column_inserted(self, column: int, num_inserted: int) -> None: ...
    def column_reordered(self) -> None: ...
    def get_caption(self) -> Object: ...
    def get_column_at_index(self, index_: int) -> int: ...
    def get_column_description(self, column: int) -> str: ...
    def get_column_extent_at(self, row: int, column: int) -> int: ...
    def get_column_header(self, column: int) -> Object: ...
    def get_index_at(self, row: int, column: int) -> int: ...
    def get_n_columns(self) -> int: ...
    def get_n_rows(self) -> int: ...
    def get_row_at_index(self, index_: int) -> int: ...
    def get_row_description(self, row: int) -> str: ...
    def get_row_extent_at(self, row: int, column: int) -> int: ...
    def get_row_header(self, row: int) -> Object: ...
    def get_selected_columns(self, selected: int) -> int: ...
    def get_selected_rows(self, selected: int) -> int: ...
    def get_summary(self) -> Object: ...
    def is_column_selected(self, column: int) -> bool: ...
    def is_row_selected(self, row: int) -> bool: ...
    def is_selected(self, row: int, column: int) -> bool: ...
    def model_changed(self) -> None: ...
    def ref_at(self, row: int, column: int) -> Object: ...
    def remove_column_selection(self, column: int) -> bool: ...
    def remove_row_selection(self, row: int) -> bool: ...
    def row_deleted(self, row: int, num_deleted: int) -> None: ...
    def row_inserted(self, row: int, num_inserted: int) -> None: ...
    def row_reordered(self) -> None: ...
    def set_caption(self, caption: Object) -> None: ...
    def set_column_description(self, column: int, description: str) -> None: ...
    def set_column_header(self, column: int, header: Object) -> None: ...
    def set_row_description(self, row: int, description: str) -> None: ...
    def set_row_header(self, row: int, header: Object) -> None: ...
    def set_summary(self, accessible: Object) -> None: ...
    def add_column_selection(self, column: int) -> bool: ...
    def add_row_selection(self, row: int) -> bool: ...
    def get_caption(self) -> Object: ...
    def get_column_at_index(self, index_: int) -> int: ...
    def get_column_description(self, column: int) -> str: ...
    def get_column_extent_at(self, row: int, column: int) -> int: ...
    def get_column_header(self, column: int) -> Object: ...
    def get_index_at(self, row: int, column: int) -> int: ...
    def get_n_columns(self) -> int: ...
    def get_n_rows(self) -> int: ...
    def get_row_at_index(self, index_: int) -> int: ...
    def get_row_description(self, row: int) -> str: ...
    def get_row_extent_at(self, row: int, column: int) -> int: ...
    def get_row_header(self, row: int) -> Object: ...
    def get_selected_columns(self, selected: int) -> int: ...
    def get_selected_rows(self, selected: int) -> int: ...
    def get_summary(self) -> Object: ...
    def is_column_selected(self, column: int) -> bool: ...
    def is_row_selected(self, row: int) -> bool: ...
    def is_selected(self, row: int, column: int) -> bool: ...
    def ref_at(self, row: int, column: int) -> Object: ...
    def remove_column_selection(self, column: int) -> bool: ...
    def remove_row_selection(self, row: int) -> bool: ...
    def set_caption(self, caption: Object) -> None: ...
    def set_column_description(self, column: int, description: str) -> None: ...
    def set_column_header(self, column: int, header: Object) -> None: ...
    def set_row_description(self, row: int, description: str) -> None: ...
    def set_row_header(self, row: int, header: Object) -> None: ...
    def set_summary(self, accessible: Object) -> None: ...
class TableCell(Object): 
    def get_column_header_cells(self) -> list[Object]: ...
    def get_column_span(self) -> int: ...
    def get_position(self, row: int, column: int) -> bool: ...
    def get_row_column_span(self, row: int, column: int, row_span: int, column_span: int) -> bool: ...
    def get_row_header_cells(self) -> list[Object]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Object: ...
    def get_column_header_cells(self) -> list[Object]: ...
    def get_column_span(self) -> int: ...
    def get_position(self, row: int, column: int) -> bool: ...
    def get_row_column_span(self, row: int, column: int, row_span: int, column_span: int) -> bool: ...
    def get_row_header_cells(self) -> list[Object]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Object: ...
class Text: 
    def add_selection(self, start_offset: int, end_offset: int) -> bool: ...
    def get_bounded_ranges(self, rect: TextRectangle, coord_type: CoordType, x_clip_type: TextClipType, y_clip_type: TextClipType) -> list[TextRange]: ...
    def get_caret_offset(self) -> int: ...
    def get_character_at_offset(self, offset: int) -> gunichar: ...
    def get_character_count(self) -> int: ...
    def get_character_extents(self, offset: int, x: int, y: int, width: int, height: int, coords: CoordType) -> None: ...
    def get_default_attributes(self) -> AttributeSet: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, coords: CoordType) -> int: ...
    def get_range_extents(self, start_offset: int, end_offset: int, coord_type: CoordType, rect: TextRectangle) -> None: ...
    def get_run_attributes(self, offset: int, start_offset: int, end_offset: int) -> AttributeSet: ...
    def get_selection(self, selection_num: int, start_offset: int, end_offset: int) -> str: ...
    def get_string_at_offset(self, offset: int, granularity: TextGranularity, start_offset: int, end_offset: int) -> str: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    def get_text_after_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def get_text_at_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def get_text_before_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def remove_selection(self, selection_num: int) -> bool: ...
    def scroll_substring_to(self, start_offset: int, end_offset: int, type: ScrollType) -> bool: ...
    def scroll_substring_to_point(self, start_offset: int, end_offset: int, coords: CoordType, x: int, y: int) -> bool: ...
    def set_caret_offset(self, offset: int) -> bool: ...
    def set_selection(self, selection_num: int, start_offset: int, end_offset: int) -> bool: ...
    def text_attributes_changed(self) -> None: ...
    def text_caret_moved(self, location: int) -> None: ...
    def text_changed(self, position: int, length: int) -> None: ...
    def text_selection_changed(self) -> None: ...
    def add_selection(self, start_offset: int, end_offset: int) -> bool: ...
    def get_bounded_ranges(self, rect: TextRectangle, coord_type: CoordType, x_clip_type: TextClipType, y_clip_type: TextClipType) -> list[TextRange]: ...
    def get_caret_offset(self) -> int: ...
    def get_character_at_offset(self, offset: int) -> gunichar: ...
    def get_character_count(self) -> int: ...
    def get_character_extents(self, offset: int, x: int, y: int, width: int, height: int, coords: CoordType) -> None: ...
    def get_default_attributes(self) -> AttributeSet: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, coords: CoordType) -> int: ...
    def get_range_extents(self, start_offset: int, end_offset: int, coord_type: CoordType, rect: TextRectangle) -> None: ...
    def get_run_attributes(self, offset: int, start_offset: int, end_offset: int) -> AttributeSet: ...
    def get_selection(self, selection_num: int, start_offset: int, end_offset: int) -> str: ...
    def get_string_at_offset(self, offset: int, granularity: TextGranularity, start_offset: int, end_offset: int) -> str: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    def get_text_after_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def get_text_at_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def get_text_before_offset(self, offset: int, boundary_type: TextBoundary, start_offset: int, end_offset: int) -> str: ...
    def remove_selection(self, selection_num: int) -> bool: ...
    def scroll_substring_to(self, start_offset: int, end_offset: int, type: ScrollType) -> bool: ...
    def scroll_substring_to_point(self, start_offset: int, end_offset: int, coords: CoordType, x: int, y: int) -> bool: ...
    def set_caret_offset(self, offset: int) -> bool: ...
    def set_selection(self, selection_num: int, start_offset: int, end_offset: int) -> bool: ...
class Value: 
    def get_current_value(self, value: GObject.Value) -> None: ...
    def get_increment(self) -> float: ...
    def get_maximum_value(self, value: GObject.Value) -> None: ...
    def get_minimum_increment(self, value: GObject.Value) -> None: ...
    def get_minimum_value(self, value: GObject.Value) -> None: ...
    def get_range(self) -> Range: ...
    def get_sub_ranges(self) -> GLib.SList: ...
    def get_value_and_text(self, value: float, text: str) -> None: ...
    def set_current_value(self, value: GObject.Value) -> bool: ...
    def set_value(self, new_value: float) -> None: ...
    def get_current_value(self, value: GObject.Value) -> None: ...
    def get_increment(self) -> float: ...
    def get_maximum_value(self, value: GObject.Value) -> None: ...
    def get_minimum_increment(self, value: GObject.Value) -> None: ...
    def get_minimum_value(self, value: GObject.Value) -> None: ...
    def get_range(self) -> Range: ...
    def get_sub_ranges(self) -> GLib.SList: ...
    def get_value_and_text(self, value: float, text: str) -> None: ...
    def set_current_value(self, value: GObject.Value) -> bool: ...
    def set_value(self, new_value: float) -> None: ...
class Window(Object): ...

class HyperlinkStateFlags(GObject.GFlag): 
    INLINE = ...

class CoordType(GObject.GEnum): 
    SCREEN = ...
    WINDOW = ...
    PARENT = ...

class KeyEventType(GObject.GEnum): 
    PRESS = ...
    RELEASE = ...
    LAST_DEFINED = ...

class Layer(GObject.GEnum): 
    INVALID = ...
    BACKGROUND = ...
    CANVAS = ...
    WIDGET = ...
    MDI = ...
    POPUP = ...
    OVERLAY = ...
    WINDOW = ...

class RelationType(GObject.GEnum): 
    NULL = ...
    CONTROLLED_BY = ...
    CONTROLLER_FOR = ...
    LABEL_FOR = ...
    LABELLED_BY = ...
    MEMBER_OF = ...
    NODE_CHILD_OF = ...
    FLOWS_TO = ...
    FLOWS_FROM = ...
    SUBWINDOW_OF = ...
    EMBEDS = ...
    EMBEDDED_BY = ...
    POPUP_FOR = ...
    PARENT_WINDOW_OF = ...
    DESCRIBED_BY = ...
    DESCRIPTION_FOR = ...
    NODE_PARENT_OF = ...
    DETAILS = ...
    DETAILS_FOR = ...
    ERROR_MESSAGE = ...
    ERROR_FOR = ...
    LAST_DEFINED = ...

class Role(GObject.GEnum): 
    INVALID = ...
    ACCELERATOR_LABEL = ...
    ALERT = ...
    ANIMATION = ...
    ARROW = ...
    CALENDAR = ...
    CANVAS = ...
    CHECK_BOX = ...
    CHECK_MENU_ITEM = ...
    COLOR_CHOOSER = ...
    COLUMN_HEADER = ...
    COMBO_BOX = ...
    DATE_EDITOR = ...
    DESKTOP_ICON = ...
    DESKTOP_FRAME = ...
    DIAL = ...
    DIALOG = ...
    DIRECTORY_PANE = ...
    DRAWING_AREA = ...
    FILE_CHOOSER = ...
    FILLER = ...
    FONT_CHOOSER = ...
    FRAME = ...
    GLASS_PANE = ...
    HTML_CONTAINER = ...
    ICON = ...
    IMAGE = ...
    INTERNAL_FRAME = ...
    LABEL = ...
    LAYERED_PANE = ...
    LIST = ...
    LIST_ITEM = ...
    MENU = ...
    MENU_BAR = ...
    MENU_ITEM = ...
    OPTION_PANE = ...
    PAGE_TAB = ...
    PAGE_TAB_LIST = ...
    PANEL = ...
    PASSWORD_TEXT = ...
    POPUP_MENU = ...
    PROGRESS_BAR = ...
    PUSH_BUTTON = ...
    RADIO_BUTTON = ...
    RADIO_MENU_ITEM = ...
    ROOT_PANE = ...
    ROW_HEADER = ...
    SCROLL_BAR = ...
    SCROLL_PANE = ...
    SEPARATOR = ...
    SLIDER = ...
    SPLIT_PANE = ...
    SPIN_BUTTON = ...
    STATUSBAR = ...
    TABLE = ...
    TABLE_CELL = ...
    TABLE_COLUMN_HEADER = ...
    TABLE_ROW_HEADER = ...
    TEAR_OFF_MENU_ITEM = ...
    TERMINAL = ...
    TEXT = ...
    TOGGLE_BUTTON = ...
    TOOL_BAR = ...
    TOOL_TIP = ...
    TREE = ...
    TREE_TABLE = ...
    UNKNOWN = ...
    VIEWPORT = ...
    WINDOW = ...
    HEADER = ...
    FOOTER = ...
    PARAGRAPH = ...
    RULER = ...
    APPLICATION = ...
    AUTOCOMPLETE = ...
    EDIT_BAR = ...
    EMBEDDED = ...
    ENTRY = ...
    CHART = ...
    CAPTION = ...
    DOCUMENT_FRAME = ...
    HEADING = ...
    PAGE = ...
    SECTION = ...
    REDUNDANT_OBJECT = ...
    FORM = ...
    LINK = ...
    INPUT_METHOD_WINDOW = ...
    TABLE_ROW = ...
    TREE_ITEM = ...
    DOCUMENT_SPREADSHEET = ...
    DOCUMENT_PRESENTATION = ...
    DOCUMENT_TEXT = ...
    DOCUMENT_WEB = ...
    DOCUMENT_EMAIL = ...
    COMMENT = ...
    LIST_BOX = ...
    GROUPING = ...
    IMAGE_MAP = ...
    NOTIFICATION = ...
    INFO_BAR = ...
    LEVEL_BAR = ...
    TITLE_BAR = ...
    BLOCK_QUOTE = ...
    AUDIO = ...
    VIDEO = ...
    DEFINITION = ...
    ARTICLE = ...
    LANDMARK = ...
    LOG = ...
    MARQUEE = ...
    MATH = ...
    RATING = ...
    TIMER = ...
    DESCRIPTION_LIST = ...
    DESCRIPTION_TERM = ...
    DESCRIPTION_VALUE = ...
    STATIC = ...
    MATH_FRACTION = ...
    MATH_ROOT = ...
    SUBSCRIPT = ...
    SUPERSCRIPT = ...
    FOOTNOTE = ...
    CONTENT_DELETION = ...
    CONTENT_INSERTION = ...
    MARK = ...
    SUGGESTION = ...
    LAST_DEFINED = ...

class ScrollType(GObject.GEnum): 
    TOP_LEFT = ...
    BOTTOM_RIGHT = ...
    TOP_EDGE = ...
    BOTTOM_EDGE = ...
    LEFT_EDGE = ...
    RIGHT_EDGE = ...
    ANYWHERE = ...

class StateType(GObject.GEnum): 
    INVALID = ...
    ACTIVE = ...
    ARMED = ...
    BUSY = ...
    CHECKED = ...
    DEFUNCT = ...
    EDITABLE = ...
    ENABLED = ...
    EXPANDABLE = ...
    EXPANDED = ...
    FOCUSABLE = ...
    FOCUSED = ...
    HORIZONTAL = ...
    ICONIFIED = ...
    MODAL = ...
    MULTI_LINE = ...
    MULTISELECTABLE = ...
    OPAQUE = ...
    PRESSED = ...
    RESIZABLE = ...
    SELECTABLE = ...
    SELECTED = ...
    SENSITIVE = ...
    SHOWING = ...
    SINGLE_LINE = ...
    STALE = ...
    TRANSIENT = ...
    VERTICAL = ...
    VISIBLE = ...
    MANAGES_DESCENDANTS = ...
    INDETERMINATE = ...
    TRUNCATED = ...
    REQUIRED = ...
    INVALID_ENTRY = ...
    SUPPORTS_AUTOCOMPLETION = ...
    SELECTABLE_TEXT = ...
    DEFAULT = ...
    ANIMATED = ...
    VISITED = ...
    CHECKABLE = ...
    HAS_POPUP = ...
    HAS_TOOLTIP = ...
    READ_ONLY = ...
    COLLAPSED = ...
    LAST_DEFINED = ...

class TextAttribute(GObject.GEnum): 
    INVALID = ...
    LEFT_MARGIN = ...
    RIGHT_MARGIN = ...
    INDENT = ...
    INVISIBLE = ...
    EDITABLE = ...
    PIXELS_ABOVE_LINES = ...
    PIXELS_BELOW_LINES = ...
    PIXELS_INSIDE_WRAP = ...
    BG_FULL_HEIGHT = ...
    RISE = ...
    UNDERLINE = ...
    STRIKETHROUGH = ...
    SIZE = ...
    SCALE = ...
    WEIGHT = ...
    LANGUAGE = ...
    FAMILY_NAME = ...
    BG_COLOR = ...
    FG_COLOR = ...
    BG_STIPPLE = ...
    FG_STIPPLE = ...
    WRAP_MODE = ...
    DIRECTION = ...
    JUSTIFICATION = ...
    STRETCH = ...
    VARIANT = ...
    STYLE = ...
    TEXT_POSITION = ...
    LAST_DEFINED = ...

class TextBoundary(GObject.GEnum): 
    CHAR = ...
    WORD_START = ...
    WORD_END = ...
    SENTENCE_START = ...
    SENTENCE_END = ...
    LINE_START = ...
    LINE_END = ...

class TextClipType(GObject.GEnum): 
    NONE = ...
    MIN = ...
    MAX = ...
    BOTH = ...

class TextGranularity(GObject.GEnum): 
    CHAR = ...
    WORD = ...
    SENTENCE = ...
    LINE = ...
    PARAGRAPH = ...

class ValueType(GObject.GEnum): 
    VERY_WEAK = ...
    WEAK = ...
    ACCEPTABLE = ...
    STRONG = ...
    VERY_STRONG = ...
    VERY_LOW = ...
    LOW = ...
    MEDIUM = ...
    HIGH = ...
    VERY_HIGH = ...
    VERY_BAD = ...
    BAD = ...
    GOOD = ...
    VERY_GOOD = ...
    BEST = ...
    LAST_DEFINED = ...

