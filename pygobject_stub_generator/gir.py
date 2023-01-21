from pygobject_stub_generator.utility import *

class GirInclude:
    name: str
    version: str

    def __init__(self, name: str, version: str) -> None:
        self.name = name
        self.version = version

class GirType:
    name: str
    is_array: bool
    is_self: bool

    def __init__(self) -> None:
        self.name = ''
        self.is_array = False
        self.is_self = False

    def get_stub(self) -> str:
        stub = get_type(self.name)
        if self.is_array:
            stub = 'list[%s]' % stub
        return stub

class GirVar:
    name: str
    gtype: GirType

    def __init__(self) -> None:
        self.name = ''
        self.gtype = GirType()

    def get_stub(self) -> None:
        if self.gtype.is_self:
            return self.name
        return '%s: %s' % (self.name, self.gtype.get_stub())

class GirFunction:
    name: str
    instance_parameter: GirVar | None
    parameters: list[GirVar]
    return_type: GirType

    def __init__(self) -> None:
        self.name = ''
        self.instance_parameter = None
        self.parameters = []   
        self.return_type = GirType()
        self.return_type.name = 'None' 

    def get_stub(self, is_classmethod=False) -> str:
        param_stubs = list(map(lambda p : p.get_stub(), self.parameters))
        if self.instance_parameter is not None:
            param_stubs.insert(0, self.instance_parameter.get_stub())
        if is_classmethod:
            param_stubs.insert(0, 'cls')
        return 'def %s(%s) -> %s: ...' % (self.name, ', '.join(param_stubs), self.return_type.get_stub())

class GirInterface:
    name: str
    prerequisite: str
    virtual_methods: list[GirFunction]
    methods: list[GirFunction]

    def __init__(self) -> None:
        self.name = ''
        self.prerequisite = ''
        self.virtual_methods = []
        self.methods = []

    def get_stub(self) -> str:
        lines = []
        prereq = '(%s)' % self.prerequisite if len(self.prerequisite) > 0 else ''
        lines.append('class %s%s: %s' % (self.name, prereq, '...' if len(self.virtual_methods) == 0 and len(self.methods) == 0 else ''))
        for m in self.virtual_methods:
            lines.append('    %s' % m.get_stub())
        for m in self.methods:
            lines.append('    %s' % m.get_stub())
        return '\n'.join(lines)

class GirClass:
    name: str
    implements: list[str]
    constructor: GirFunction | None
    functions: list[GirFunction]
    methods: list[GirFunction]
    properties: list[GirVar]

    def __init__(self) -> None:
        self.name = ''
        self.implements = []
        self.constructor = None
        self.functions = []
        self.methods = []
        self.properties = []

    def get_stub(self) -> str:
        lines = []
        impl = '(%s)' % ', '.join(self.implements) if len(self.implements) > 0 else ''
        lines.append('class %s%s: %s' % (self.name, impl, '...' if self.constructor == None and len(self.functions) == 0 and len(self.methods) == 0 else ''))
        if self.constructor is not None:
            lines.append('    @classmethod')
            lines.append('    %s' % self.constructor.get_stub(is_classmethod=True))
        for m in self.functions:
            lines.append('    @classmethod')
            lines.append('    %s' % m.get_stub(is_classmethod=True))
        for m in self.methods:
            lines.append('    %s' % m.get_stub())
        return '\n'.join(lines)

class GirEnumeration:
    name: str
    members: list[str]
    is_flag: bool
    
    def __init__(self) -> None:
        self.name = ''
        self.members = []
        self.is_flag = False

    def get_stub(self) -> str:
        lines = []
        lines.append('class %s(GObject.G%s): %s' % (self.name, 'Flag' if self.is_flag else 'Enum', '...' if self.members == 0 else ''))
        for m in self.members:
            lines.append('    %s = ...' % m.upper())
        return '\n'.join(lines)

class Gir:
    name: str
    version: str
    includes: list[GirInclude]
    constants: list[GirVar]
    functions: list[GirFunction]
    interfaces: list[GirInterface]
    classes: list[GirClass]
    bitfields: list[GirEnumeration]
    enumerations: list[GirEnumeration]
    
    def __init__(self) -> None:
        self.name = ''
        self.version = ''
        self.includes = []
        self.constants = []
        self.functions = []
        self.interfaces = []
        self.classes = []
        self.bitfields = []
        self.enumerations = []