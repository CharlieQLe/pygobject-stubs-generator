from gi.repository import GLib, GLib, GObject

PARAM_MASK: int
PARAM_STATIC_STRINGS: int
PARAM_USER_SHIFT: int
SIGNAL_FLAGS_MASK: int
SIGNAL_MATCH_MASK: int
TYPE_FLAG_RESERVED_ID_BIT: GLib.Type
TYPE_FUNDAMENTAL_MAX: int
TYPE_FUNDAMENTAL_SHIFT: int
TYPE_RESERVED_BSE_FIRST: int
TYPE_RESERVED_BSE_LAST: int
TYPE_RESERVED_GLIB_FIRST: int
TYPE_RESERVED_GLIB_LAST: int
TYPE_RESERVED_USER_FIRST: int
VALUE_INTERNED_STRING: int
VALUE_NOCOPY_CONTENTS: int

def boxed_copy(boxed_type: GObject.Type, src_boxed: object) -> object: ...
def boxed_free(boxed_type: GObject.Type, boxed: object) -> None: ...
def boxed_type_register_static(name: str, boxed_copy: BoxedCopyFunc, boxed_free: BoxedFreeFunc) -> GObject.Type: ...
def cclosure_marshal_BOOLEAN__BOXED_BOXED(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_BOOLEAN__FLAGS(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_STRING__OBJECT_POINTER(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__BOOLEAN(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__BOXED(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__CHAR(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__DOUBLE(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__ENUM(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__FLAGS(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__FLOAT(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__INT(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__LONG(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__OBJECT(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__PARAM(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__POINTER(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__STRING(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__UCHAR(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__UINT(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__UINT_POINTER(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__ULONG(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__VARIANT(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_VOID__VOID(closure: Closure, return_value: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_marshal_generic(closure: Closure, return_gvalue: Value, n_param_values: int, param_values: Value, invocation_hint: object, marshal_data: object) -> None: ...
def cclosure_new(callback_func: Callback, user_data: object, destroy_data: ClosureNotify) -> Closure: ...
def cclosure_new_object(callback_func: Callback, object: Object) -> Closure: ...
def cclosure_new_object_swap(callback_func: Callback, object: Object) -> Closure: ...
def cclosure_new_swap(callback_func: Callback, user_data: object, destroy_data: ClosureNotify) -> Closure: ...
def clear_object(object_ptr: Object) -> None: ...
def clear_signal_handler(handler_id_ptr: int, instance: Object) -> None: ...
def enum_complete_type_info(g_enum_type: GObject.Type, info: TypeInfo, const_values: EnumValue) -> None: ...
def enum_get_value(enum_class: EnumClass, value: int) -> EnumValue: ...
def enum_get_value_by_name(enum_class: EnumClass, name: str) -> EnumValue: ...
def enum_get_value_by_nick(enum_class: EnumClass, nick: str) -> EnumValue: ...
def enum_register_static(name: str, const_static_values: EnumValue) -> GObject.Type: ...
def enum_to_string(g_enum_type: GObject.Type, value: int) -> str: ...
def flags_complete_type_info(g_flags_type: GObject.Type, info: TypeInfo, const_values: FlagsValue) -> None: ...
def flags_get_first_value(flags_class: FlagsClass, value: int) -> FlagsValue: ...
def flags_get_value_by_name(flags_class: FlagsClass, name: str) -> FlagsValue: ...
def flags_get_value_by_nick(flags_class: FlagsClass, nick: str) -> FlagsValue: ...
def flags_register_static(name: str, const_static_values: FlagsValue) -> GObject.Type: ...
def flags_to_string(flags_type: GObject.Type, value: int) -> str: ...
def gtype_get_type() -> GObject.Type: ...
def param_spec_boolean(name: str, nick: str, blurb: str, default_value: bool, flags: ParamFlags) -> ParamSpec: ...
def param_spec_boxed(name: str, nick: str, blurb: str, boxed_type: GObject.Type, flags: ParamFlags) -> ParamSpec: ...
def param_spec_char(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_double(name: str, nick: str, blurb: str, minimum: float, maximum: float, default_value: float, flags: ParamFlags) -> ParamSpec: ...
def param_spec_enum(name: str, nick: str, blurb: str, enum_type: GObject.Type, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_flags(name: str, nick: str, blurb: str, flags_type: GObject.Type, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_float(name: str, nick: str, blurb: str, minimum: float, maximum: float, default_value: float, flags: ParamFlags) -> ParamSpec: ...
def param_spec_gtype(name: str, nick: str, blurb: str, is_a_type: GObject.Type, flags: ParamFlags) -> ParamSpec: ...
def param_spec_int(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_int64(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_long(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_object(name: str, nick: str, blurb: str, object_type: GObject.Type, flags: ParamFlags) -> ParamSpec: ...
def param_spec_override(name: str, overridden: ParamSpec) -> ParamSpec: ...
def param_spec_param(name: str, nick: str, blurb: str, param_type: GObject.Type, flags: ParamFlags) -> ParamSpec: ...
def param_spec_pointer(name: str, nick: str, blurb: str, flags: ParamFlags) -> ParamSpec: ...
def param_spec_string(name: str, nick: str, blurb: str, default_value: str, flags: ParamFlags) -> ParamSpec: ...
def param_spec_uchar(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_uint(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_uint64(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_ulong(name: str, nick: str, blurb: str, minimum: int, maximum: int, default_value: int, flags: ParamFlags) -> ParamSpec: ...
def param_spec_unichar(name: str, nick: str, blurb: str, default_value: gunichar, flags: ParamFlags) -> ParamSpec: ...
def param_spec_value_array(name: str, nick: str, blurb: str, element_spec: ParamSpec, flags: ParamFlags) -> ParamSpec: ...
def param_spec_variant(name: str, nick: str, blurb: str, type: GLib.VariantType, default_value: GLib.Variant, flags: ParamFlags) -> ParamSpec: ...
def param_type_register_static(name: str, pspec_info: ParamSpecTypeInfo) -> GObject.Type: ...
def param_value_convert(pspec: ParamSpec, src_value: Value, dest_value: Value, strict_validation: bool) -> bool: ...
def param_value_defaults(pspec: ParamSpec, value: Value) -> bool: ...
def param_value_is_valid(pspec: ParamSpec, value: Value) -> bool: ...
def param_value_set_default(pspec: ParamSpec, value: Value) -> None: ...
def param_value_validate(pspec: ParamSpec, value: Value) -> bool: ...
def param_values_cmp(pspec: ParamSpec, value1: Value, value2: Value) -> int: ...
def pointer_type_register_static(name: str) -> GObject.Type: ...
def signal_accumulator_first_wins(ihint: SignalInvocationHint, return_accu: Value, handler_return: Value, dummy: object) -> bool: ...
def signal_accumulator_true_handled(ihint: SignalInvocationHint, return_accu: Value, handler_return: Value, dummy: object) -> bool: ...
def signal_add_emission_hook(signal_id: int, detail: GLib.Quark, hook_func: SignalEmissionHook, hook_data: object, data_destroy: GLib.DestroyNotify) -> int: ...
def signal_chain_from_overridden(instance_and_params: list[Value], return_value: Value) -> None: ...
def signal_chain_from_overridden_handler(instance: TypeInstance) -> None: ...
def signal_connect_closure(instance: Object, detailed_signal: str, closure: Closure, after: bool) -> int: ...
def signal_connect_closure_by_id(instance: Object, signal_id: int, detail: GLib.Quark, closure: Closure, after: bool) -> int: ...
def signal_connect_data(instance: Object, detailed_signal: str, c_handler: Callback, data: object, destroy_data: ClosureNotify, connect_flags: ConnectFlags) -> int: ...
def signal_connect_object(instance: TypeInstance, detailed_signal: str, c_handler: Callback, gobject: Object, connect_flags: ConnectFlags) -> int: ...
def signal_emit(instance: Object, signal_id: int, detail: GLib.Quark) -> None: ...
def signal_emit_by_name(instance: Object, detailed_signal: str) -> None: ...
def signal_emit_valist(instance: TypeInstance, signal_id: int, detail: GLib.Quark, var_args: va_list) -> None: ...
def signal_emitv(instance_and_params: list[Value], signal_id: int, detail: GLib.Quark, return_value: Value) -> None: ...
def signal_get_invocation_hint(instance: Object) -> SignalInvocationHint: ...
def signal_handler_block(instance: Object, handler_id: int) -> None: ...
def signal_handler_disconnect(instance: Object, handler_id: int) -> None: ...
def signal_handler_find(instance: Object, mask: SignalMatchType, signal_id: int, detail: GLib.Quark, closure: Closure, func: object, data: object) -> int: ...
def signal_handler_is_connected(instance: Object, handler_id: int) -> bool: ...
def signal_handler_unblock(instance: Object, handler_id: int) -> None: ...
def signal_handlers_block_matched(instance: Object, mask: SignalMatchType, signal_id: int, detail: GLib.Quark, closure: Closure, func: object, data: object) -> int: ...
def signal_handlers_destroy(instance: Object) -> None: ...
def signal_handlers_disconnect_matched(instance: Object, mask: SignalMatchType, signal_id: int, detail: GLib.Quark, closure: Closure, func: object, data: object) -> int: ...
def signal_handlers_unblock_matched(instance: Object, mask: SignalMatchType, signal_id: int, detail: GLib.Quark, closure: Closure, func: object, data: object) -> int: ...
def signal_has_handler_pending(instance: Object, signal_id: int, detail: GLib.Quark, may_be_blocked: bool) -> bool: ...
def signal_is_valid_name(name: str) -> bool: ...
def signal_list_ids(itype: GObject.Type, n_ids: int) -> list[int]: ...
def signal_lookup(name: str, itype: GObject.Type) -> int: ...
def signal_name(signal_id: int) -> str: ...
def signal_new(signal_name: str, itype: GObject.Type, signal_flags: SignalFlags, class_offset: int, accumulator: SignalAccumulator, accu_data: object, c_marshaller: SignalCMarshaller, return_type: GObject.Type, n_params: int) -> int: ...
def signal_new_class_handler(signal_name: str, itype: GObject.Type, signal_flags: SignalFlags, class_handler: Callback, accumulator: SignalAccumulator, accu_data: object, c_marshaller: SignalCMarshaller, return_type: GObject.Type, n_params: int) -> int: ...
def signal_new_valist(signal_name: str, itype: GObject.Type, signal_flags: SignalFlags, class_closure: Closure, accumulator: SignalAccumulator, accu_data: object, c_marshaller: SignalCMarshaller, return_type: GObject.Type, n_params: int, args: va_list) -> int: ...
def signal_newv(signal_name: str, itype: GObject.Type, signal_flags: SignalFlags, class_closure: Closure, accumulator: SignalAccumulator, accu_data: object, c_marshaller: SignalCMarshaller, return_type: GObject.Type, n_params: int, param_types: list[GObject.Type]) -> int: ...
def signal_override_class_closure(signal_id: int, instance_type: GObject.Type, class_closure: Closure) -> None: ...
def signal_override_class_handler(signal_name: str, instance_type: GObject.Type, class_handler: Callback) -> None: ...
def signal_parse_name(detailed_signal: str, itype: GObject.Type, signal_id_p: int, detail_p: GLib.Quark, force_detail_quark: bool) -> bool: ...
def signal_query(signal_id: int, query: SignalQuery) -> None: ...
def signal_remove_emission_hook(signal_id: int, hook_id: int) -> None: ...
def signal_set_va_marshaller(signal_id: int, instance_type: GObject.Type, va_marshaller: SignalCVaMarshaller) -> None: ...
def signal_stop_emission(instance: Object, signal_id: int, detail: GLib.Quark) -> None: ...
def signal_stop_emission_by_name(instance: Object, detailed_signal: str) -> None: ...
def signal_type_cclosure_new(itype: GObject.Type, struct_offset: int) -> Closure: ...
def source_set_closure(source: GLib.Source, closure: Closure) -> None: ...
def source_set_dummy_callback(source: GLib.Source) -> None: ...
def strdup_value_contents(value: Value) -> str: ...
def type_add_class_cache_func(cache_data: object, cache_func: TypeClassCacheFunc) -> None: ...
def type_add_class_private(class_type: GObject.Type, private_size: gsize) -> None: ...
def type_add_instance_private(class_type: GObject.Type, private_size: gsize) -> int: ...
def type_add_interface_check(check_data: object, check_func: TypeInterfaceCheckFunc) -> None: ...
def type_add_interface_dynamic(instance_type: GObject.Type, interface_type: GObject.Type, plugin: TypePlugin) -> None: ...
def type_add_interface_static(instance_type: GObject.Type, interface_type: GObject.Type, info: InterfaceInfo) -> None: ...
def type_check_class_cast(g_class: TypeClass, is_a_type: GObject.Type) -> TypeClass: ...
def type_check_class_is_a(g_class: TypeClass, is_a_type: GObject.Type) -> bool: ...
def type_check_instance(instance: TypeInstance) -> bool: ...
def type_check_instance_cast(instance: TypeInstance, iface_type: GObject.Type) -> TypeInstance: ...
def type_check_instance_is_a(instance: TypeInstance, iface_type: GObject.Type) -> bool: ...
def type_check_instance_is_fundamentally_a(instance: TypeInstance, fundamental_type: GObject.Type) -> bool: ...
def type_check_is_value_type(type: GObject.Type) -> bool: ...
def type_check_value(value: Value) -> bool: ...
def type_check_value_holds(value: Value, type: GObject.Type) -> bool: ...
def type_children(type: GObject.Type, n_children: int) -> list[GObject.Type]: ...
def type_class_adjust_private_offset(g_class: object, private_size_or_offset: int) -> None: ...
def type_class_peek(type: GObject.Type) -> TypeClass: ...
def type_class_peek_static(type: GObject.Type) -> TypeClass: ...
def type_class_ref(type: GObject.Type) -> TypeClass: ...
def type_create_instance(type: GObject.Type) -> TypeInstance: ...
def type_default_interface_peek(g_type: GObject.Type) -> TypeInterface: ...
def type_default_interface_ref(g_type: GObject.Type) -> TypeInterface: ...
def type_default_interface_unref(g_iface: TypeInterface) -> None: ...
def type_depth(type: GObject.Type) -> int: ...
def type_ensure(type: GObject.Type) -> None: ...
def type_free_instance(instance: TypeInstance) -> None: ...
def type_from_name(name: str) -> GObject.Type: ...
def type_fundamental(type_id: GObject.Type) -> GObject.Type: ...
def type_fundamental_next() -> GObject.Type: ...
def type_get_instance_count(type: GObject.Type) -> int: ...
def type_get_plugin(type: GObject.Type) -> TypePlugin: ...
def type_get_qdata(type: GObject.Type, quark: GLib.Quark) -> object: ...
def type_get_type_registration_serial() -> int: ...
def type_init() -> None: ...
def type_init_with_debug_flags(debug_flags: TypeDebugFlags) -> None: ...
def type_interface_add_prerequisite(interface_type: GObject.Type, prerequisite_type: GObject.Type) -> None: ...
def type_interface_get_plugin(instance_type: GObject.Type, interface_type: GObject.Type) -> TypePlugin: ...
def type_interface_instantiatable_prerequisite(interface_type: GObject.Type) -> GObject.Type: ...
def type_interface_peek(instance_class: TypeClass, iface_type: GObject.Type) -> TypeInterface: ...
def type_interface_prerequisites(interface_type: GObject.Type, n_prerequisites: int) -> list[GObject.Type]: ...
def type_interfaces(type: GObject.Type, n_interfaces: int) -> list[GObject.Type]: ...
def type_is_a(type: GObject.Type, is_a_type: GObject.Type) -> bool: ...
def type_name(type: GObject.Type) -> str: ...
def type_name_from_class(g_class: TypeClass) -> str: ...
def type_name_from_instance(instance: TypeInstance) -> str: ...
def type_next_base(leaf_type: GObject.Type, root_type: GObject.Type) -> GObject.Type: ...
def type_parent(type: GObject.Type) -> GObject.Type: ...
def type_qname(type: GObject.Type) -> GLib.Quark: ...
def type_query(type: GObject.Type, query: TypeQuery) -> None: ...
def type_register_dynamic(parent_type: GObject.Type, type_name: str, plugin: TypePlugin, flags: TypeFlags) -> GObject.Type: ...
def type_register_fundamental(type_id: GObject.Type, type_name: str, info: TypeInfo, finfo: TypeFundamentalInfo, flags: TypeFlags) -> GObject.Type: ...
def type_register_static(parent_type: GObject.Type, type_name: str, info: TypeInfo, flags: TypeFlags) -> GObject.Type: ...
def type_register_static_simple(parent_type: GObject.Type, type_name: str, class_size: int, class_init: ClassInitFunc, instance_size: int, instance_init: InstanceInitFunc, flags: TypeFlags) -> GObject.Type: ...
def type_remove_class_cache_func(cache_data: object, cache_func: TypeClassCacheFunc) -> None: ...
def type_remove_interface_check(check_data: object, check_func: TypeInterfaceCheckFunc) -> None: ...
def type_set_qdata(type: GObject.Type, quark: GLib.Quark, data: object) -> None: ...
def type_test_flags(type: GObject.Type, flags: int) -> bool: ...
def type_value_table_peek(type: GObject.Type) -> TypeValueTable: ...
def value_register_transform_func(src_type: GObject.Type, dest_type: GObject.Type, transform_func: ValueTransform) -> None: ...
def value_type_compatible(src_type: GObject.Type, dest_type: GObject.Type) -> bool: ...
def value_type_transformable(src_type: GObject.Type, dest_type: GObject.Type) -> bool: ...

class Binding(Object): 
    def dup_source(self) -> Object: ...
    def dup_target(self) -> Object: ...
    def get_flags(self) -> BindingFlags: ...
    def get_source(self) -> Object: ...
    def get_source_property(self) -> str: ...
    def get_target(self) -> Object: ...
    def get_target_property(self) -> str: ...
    def unbind(self) -> None: ...

class BindingGroup(Object): 
    @classmethod
    def new(cls) -> BindingGroup: ...
    def bind(self, source_property: str, target: Object, target_property: str, flags: BindingFlags) -> None: ...
    def bind_full(self, source_property: str, target: Object, target_property: str, flags: BindingFlags, transform_to: BindingTransformFunc, transform_from: BindingTransformFunc, user_data: object, user_data_destroy: GLib.DestroyNotify) -> None: ...
    def bind_with_closures(self, source_property: str, target: Object, target_property: str, flags: BindingFlags, transform_to: Closure, transform_from: Closure) -> None: ...
    def dup_source(self) -> Object: ...
    def set_source(self, source: Object) -> None: ...

class InitiallyUnowned(Object): ...

class Object: 
    @classmethod
    def new(cls, object_type: GObject.Type, first_property_name: str) -> Object: ...
    @classmethod
    def compat_control(cls, what: gsize, data: object) -> gsize: ...
    @classmethod
    def interface_find_property(cls, g_iface: TypeInterface, property_name: str) -> ParamSpec: ...
    @classmethod
    def interface_install_property(cls, g_iface: TypeInterface, pspec: ParamSpec) -> None: ...
    @classmethod
    def interface_list_properties(cls, g_iface: TypeInterface, n_properties_p: int) -> list[ParamSpec]: ...
    def add_toggle_ref(self, notify: ToggleNotify, data: object) -> None: ...
    def add_weak_pointer(self, weak_pointer_location: object) -> None: ...
    def bind_property(self, source_property: str, target: Object, target_property: str, flags: BindingFlags) -> Binding: ...
    def bind_property_full(self, source_property: str, target: Object, target_property: str, flags: BindingFlags, transform_to: BindingTransformFunc, transform_from: BindingTransformFunc, user_data: object, notify: GLib.DestroyNotify) -> Binding: ...
    def bind_property_with_closures(self, source_property: str, target: Object, target_property: str, flags: BindingFlags, transform_to: Closure, transform_from: Closure) -> Binding: ...
    def connect(self, signal_spec: str) -> Object: ...
    def disconnect(self, signal_spec: str) -> None: ...
    def dup_data(self, key: str, dup_func: GLib.DuplicateFunc, user_data: object) -> object: ...
    def dup_qdata(self, quark: GLib.Quark, dup_func: GLib.DuplicateFunc, user_data: object) -> object: ...
    def force_floating(self) -> None: ...
    def freeze_notify(self) -> None: ...
    def get(self, first_property_name: str) -> None: ...
    def get_data(self, key: str) -> object: ...
    def get_property(self, property_name: str, value: Value) -> None: ...
    def get_qdata(self, quark: GLib.Quark) -> object: ...
    def get_valist(self, first_property_name: str, var_args: va_list) -> None: ...
    def getv(self, n_properties: int, names: list[str], values: list[Value]) -> None: ...
    def is_floating(self) -> bool: ...
    def notify(self, property_name: str) -> None: ...
    def notify_by_pspec(self, pspec: ParamSpec) -> None: ...
    def ref(self) -> Object: ...
    def ref_sink(self) -> Object: ...
    def remove_toggle_ref(self, notify: ToggleNotify, data: object) -> None: ...
    def remove_weak_pointer(self, weak_pointer_location: object) -> None: ...
    def replace_data(self, key: str, oldval: object, newval: object, destroy: GLib.DestroyNotify, old_destroy: GLib.DestroyNotify) -> bool: ...
    def replace_qdata(self, quark: GLib.Quark, oldval: object, newval: object, destroy: GLib.DestroyNotify, old_destroy: GLib.DestroyNotify) -> bool: ...
    def run_dispose(self) -> None: ...
    def set(self, first_property_name: str) -> None: ...
    def set_data(self, key: str, data: object) -> None: ...
    def set_data_full(self, key: str, data: object, destroy: GLib.DestroyNotify) -> None: ...
    def set_property(self, property_name: str, value: Value) -> None: ...
    def set_qdata(self, quark: GLib.Quark, data: object) -> None: ...
    def set_qdata_full(self, quark: GLib.Quark, data: object, destroy: GLib.DestroyNotify) -> None: ...
    def set_valist(self, first_property_name: str, var_args: va_list) -> None: ...
    def setv(self, n_properties: int, names: list[str], values: list[Value]) -> None: ...
    def steal_data(self, key: str) -> object: ...
    def steal_qdata(self, quark: GLib.Quark) -> object: ...
    def take_ref(self) -> Object: ...
    def thaw_notify(self) -> None: ...
    def unref(self) -> None: ...
    def watch_closure(self, closure: Closure) -> None: ...
    def weak_ref(self, notify: WeakNotify, data: object) -> None: ...
    def weak_unref(self, notify: WeakNotify, data: object) -> None: ...

class ParamSpec: 
    @classmethod
    def internal(cls, param_type: GObject.Type, name: str, nick: str, blurb: str, flags: ParamFlags) -> ParamSpec: ...
    @classmethod
    def is_valid_name(cls, name: str) -> bool: ...
    def get_blurb(self) -> str: ...
    def get_default_value(self) -> Value: ...
    def get_name(self) -> str: ...
    def get_name_quark(self) -> GLib.Quark: ...
    def get_nick(self) -> str: ...
    def get_qdata(self, quark: GLib.Quark) -> object: ...
    def get_redirect_target(self) -> ParamSpec: ...
    def ref(self) -> ParamSpec: ...
    def ref_sink(self) -> ParamSpec: ...
    def set_qdata(self, quark: GLib.Quark, data: object) -> None: ...
    def set_qdata_full(self, quark: GLib.Quark, data: object, destroy: GLib.DestroyNotify) -> None: ...
    def sink(self) -> None: ...
    def steal_qdata(self, quark: GLib.Quark) -> object: ...
    def unref(self) -> None: ...

class ParamSpecBoolean(ParamSpec): ...

class ParamSpecBoxed(ParamSpec): ...

class ParamSpecChar(ParamSpec): ...

class ParamSpecDouble(ParamSpec): ...

class ParamSpecEnum(ParamSpec): ...

class ParamSpecFlags(ParamSpec): ...

class ParamSpecFloat(ParamSpec): ...

class ParamSpecGType(ParamSpec): ...

class ParamSpecInt(ParamSpec): ...

class ParamSpecInt64(ParamSpec): ...

class ParamSpecLong(ParamSpec): ...

class ParamSpecObject(ParamSpec): ...

class ParamSpecOverride(ParamSpec): ...

class ParamSpecParam(ParamSpec): ...

class ParamSpecPointer(ParamSpec): ...

class ParamSpecString(ParamSpec): ...

class ParamSpecUChar(ParamSpec): ...

class ParamSpecUInt(ParamSpec): ...

class ParamSpecUInt64(ParamSpec): ...

class ParamSpecULong(ParamSpec): ...

class ParamSpecUnichar(ParamSpec): ...

class ParamSpecValueArray(ParamSpec): ...

class ParamSpecVariant(ParamSpec): ...

class SignalGroup(Object): 
    @classmethod
    def new(cls, target_type: GObject.Type) -> SignalGroup: ...
    def block(self) -> None: ...
    def connect(self, detailed_signal: str, c_handler: Callback, data: object) -> None: ...
    def connect_after(self, detailed_signal: str, c_handler: Callback, data: object) -> None: ...
    def connect_closure(self, detailed_signal: str, closure: Closure, after: bool) -> None: ...
    def connect_data(self, detailed_signal: str, c_handler: Callback, data: object, notify: ClosureNotify, flags: ConnectFlags) -> None: ...
    def connect_object(self, detailed_signal: str, c_handler: Callback, object: object, flags: ConnectFlags) -> None: ...
    def connect_swapped(self, detailed_signal: str, c_handler: Callback, data: object) -> None: ...
    def dup_target(self) -> Object: ...
    def set_target(self, target: Object) -> None: ...
    def unblock(self) -> None: ...

class TypeModule(Object, TypePlugin): 
    def add_interface(self, instance_type: GObject.Type, interface_type: GObject.Type, interface_info: InterfaceInfo) -> None: ...
    def register_enum(self, name: str, const_static_values: EnumValue) -> GObject.Type: ...
    def register_flags(self, name: str, const_static_values: FlagsValue) -> GObject.Type: ...
    def register_type(self, parent_type: GObject.Type, type_name: str, type_info: TypeInfo, flags: TypeFlags) -> GObject.Type: ...
    def set_name(self, name: str) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> bool: ...

class TypePlugin: 
    def complete_interface_info(self, instance_type: GObject.Type, interface_type: GObject.Type, info: InterfaceInfo) -> None: ...
    def complete_type_info(self, g_type: GObject.Type, info: TypeInfo, value_table: TypeValueTable) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> None: ...

class BindingFlags(GObject.GFlag): 
    DEFAULT = ...
    BIDIRECTIONAL = ...
    SYNC_CREATE = ...
    INVERT_BOOLEAN = ...

class ConnectFlags(GObject.GFlag): 
    DEFAULT = ...
    AFTER = ...
    SWAPPED = ...

class ParamFlags(GObject.GFlag): 
    READABLE = ...
    WRITABLE = ...
    READWRITE = ...
    CONSTRUCT = ...
    CONSTRUCT_ONLY = ...
    LAX_VALIDATION = ...
    STATIC_NAME = ...
    PRIVATE = ...
    STATIC_NICK = ...
    STATIC_BLURB = ...
    EXPLICIT_NOTIFY = ...
    DEPRECATED = ...

class SignalFlags(GObject.GFlag): 
    RUN_FIRST = ...
    RUN_LAST = ...
    RUN_CLEANUP = ...
    NO_RECURSE = ...
    DETAILED = ...
    ACTION = ...
    NO_HOOKS = ...
    MUST_COLLECT = ...
    DEPRECATED = ...
    ACCUMULATOR_FIRST_RUN = ...

class SignalMatchType(GObject.GFlag): 
    ID = ...
    DETAIL = ...
    CLOSURE = ...
    FUNC = ...
    DATA = ...
    UNBLOCKED = ...

class TypeDebugFlags(GObject.GFlag): 
    NONE = ...
    OBJECTS = ...
    SIGNALS = ...
    INSTANCE_COUNT = ...
    MASK = ...

class TypeFlags(GObject.GFlag): 
    NONE = ...
    ABSTRACT = ...
    VALUE_ABSTRACT = ...
    FINAL = ...

class TypeFundamentalFlags(GObject.GFlag): 
    CLASSED = ...
    INSTANTIATABLE = ...
    DERIVABLE = ...
    DEEP_DERIVABLE = ...

