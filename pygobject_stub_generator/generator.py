import os
import shutil
import xml.etree.ElementTree as ET
from pygobject_stub_generator.gir import *
from pygobject_stub_generator.handle import *
from pygobject_stub_generator.writer import *

INDENT = '    '
GIR_DIR = '/usr/share/gir-1.0'

def generate() -> None:
    if os.path.isdir('out_stubs'):
        shutil.rmtree('out_stubs')
    os.mkdir('out_stubs')

    for f in os.listdir(GIR_DIR):
        filename, file_extension = os.path.splitext(f)
        if file_extension != '.gir':
            continue
        path = os.path.join(GIR_DIR, f)
        with open(path, 'r', encoding='utf-8') as reader:
            contents = reader.read()

        xml = ET.fromstring(contents)
        gir_obj = Gir()
        print('Generating stubs for %s...' % filename)

        # Handle namespace
        namespace = find_element(xml, 'namespace')
        if namespace is not None:
            handle_namespace(namespace, gir_obj)
        
        # Handle includes
        for include in find_elements(xml, 'include'):
            gir_obj.includes.append(handle_includes(include))

        # Add GObject if necessary
        if (len(gir_obj.enumerations) > 0 or len(gir_obj.bitfields) > 0) and 'GObject' not in map(lambda x: x.name, gir_obj.includes):
            gir_obj.includes.append(GirInclude('GObject', ''))

        # Generate stub
        with open('out_stubs/%s.pyi' % filename, 'w') as writer:
            write_includes(gir_obj, writer)
            write_constants(gir_obj, writer)
            write_functions(gir_obj, writer)
            write_classes(gir_obj, writer)
            write_interfaces(gir_obj, writer)
            write_bitfields(gir_obj, writer)
            write_enumerations(gir_obj, writer)