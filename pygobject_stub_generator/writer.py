from io import TextIOWrapper

from pygobject_stub_generator.gir import *
from pygobject_stub_generator.utility import *

def write_includes(gir: Gir, writer: TextIOWrapper) -> None:
    includes = ''
    for i in gir.includes:
        if len(includes) > 0:
            includes = '%s, ' % includes
        includes = '%s%s' % (includes, i.name)
    if len(includes) > 0:
        writer.write('from gi.repository import %s\n\n' % includes)

def write_constants(gir: Gir, writer: TextIOWrapper) -> None:
    constants = ''
    for c in gir.constants:
        constants = '%s%s\n' % (constants, c.get_stub())
    if len(constants) > 0:
        writer.write('%s\n' % constants)

def write_functions(gir: Gir, writer: TextIOWrapper) -> None:
    for f in gir.functions:
        writer.write('%s\n' % f.get_stub())
    writer.write('\n')

def write_classes(gir: Gir, writer: TextIOWrapper) -> None:
    for c in gir.classes:
        writer.write('%s\n\n' % c.get_stub())

def write_interfaces(gir: Gir, writer: TextIOWrapper) -> None:
    interfaces = ''
    for i in gir.interfaces:
        interfaces = '%s%s\n' % (interfaces, i.get_stub()) # TODO
    if len(interfaces) > 0:
        writer.write('%s\n' % interfaces)

def write_bitfields(gir: Gir, writer: TextIOWrapper) -> None:
    for b in gir.bitfields:
        writer.write('%s\n\n' % b.get_stub())

def write_enumerations(gir: Gir, writer: TextIOWrapper) -> None:
    for e in gir.enumerations:
        writer.write('%s\n\n' % e.get_stub())