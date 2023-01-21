import xml.etree.ElementTree as ET

from pygobject_stub_generator.gir import *
from pygobject_stub_generator.utility import *

def __handle_function_includes(f: GirFunction, gir: Gir) -> None:
    for p in filter(lambda p: '.' in p.gtype.name, f.parameters):
        typename = p.gtype.name[:p.gtype.name.index('.')]
        if typename not in map(lambda i : i.name, gir.includes):
            gir.includes.append(GirInclude(typename, ''))
    if '.' in f.return_type.name:
        typename = f.return_type.name[:f.return_type.name.index('.')]
        if typename not in map(lambda i : i.name, gir.includes):
            gir.includes.append(GirInclude(typename, ''))

def __handle_type(element: ET.Element, gtype: GirType) -> None:
    def handle(element_source: ET.Element) -> None:
        element_type = find_element(element_source, 'type')
        gtype.is_nullable = 'nullable' in element.attrib and element.attrib['nullable'] == '1'
        if element_type is not None:
            gtype.name = element_type.attrib['name']
            
    element_array = find_element(element, 'array')
    if element_array is None:
        handle(element)
    else:
        gtype.is_array = True
        handle(element_array)

def handle_includes(element: ET.Element) -> GirInclude | None:
    return GirInclude(element.attrib['name'], element.attrib['version'])
    
def handle_constant(constant: ET.Element) -> GirVar | None:
    element_type = find_element(constant, 'type')
    if element_type is not None:
        var = GirVar()
        var.name = fix_name(constant.attrib['name'])
        __handle_type(constant, var.gtype)
        #var.gtype.name = element_type.attrib['name']
        return var
    return None

def handle_function(function: ET.Element) -> GirFunction:
    gir_function = GirFunction()
    gir_function.name = function.attrib['name']

    element_parameters = find_element(function, 'parameters')
    if element_parameters is not None:
        element_instance_parameter = find_element(element_parameters, 'instance-parameter')
        if element_instance_parameter is not None:
            gir_function.instance_parameter = GirVar()
            gir_function.instance_parameter.name = 'self'
            gir_function.instance_parameter.gtype.is_self = True

        for p in find_elements(element_parameters, 'parameter'):
            if p.attrib['name'] == '...':
                continue
            var = GirVar()
            var.name = fix_name(p.attrib['name'])
            __handle_type(p, var.gtype)
            #element_array = find_element(p, 'array')
            #if element_array is None:
            #    element_type = find_element(p, 'type')
            #    if element_type is not None:
            #        var.gtype.name = element_type.attrib['name']
            #else:
            #    var.gtype.is_array = True
            #    element_type = find_element(element_array, 'type')
            #    if element_type is not None:
            #        var.gtype.name = element_type.attrib['name']
            gir_function.parameters.append(var)

    element_return_value = find_element(function, 'return-value')
    if element_return_value is not None:
        __handle_type(element_return_value, gir_function.return_type)
        #element_array = find_element(element_return_value, 'array')
        #if element_array is None:
        #    element_type = find_element(element_return_value, 'type')
        #    if element_type is not None and 'name' in element_type.attrib:
        #        gir_function.return_type.name = element_type.attrib['name']
        #else:
        #    gir_function.return_type.is_array = True
        #    element_type = find_element(element_array, 'type')
        #    if element_type is not None and 'name' in element_type.attrib:
        #        gir_function.return_type.name = element_type.attrib['name']
    return gir_function

def handle_interface(interface: ET.Element) -> GirInterface | None:
    element_prerequisite = find_element(interface, 'prerequisite')
    
    gir_interface = GirInterface()
    gir_interface.name = interface.attrib['name']
    gir_interface.prerequisite = '' if element_prerequisite is None else element_prerequisite.attrib['name']

    for m in find_elements(interface, 'virtual-method'):
        try:
            gir_interface.virtual_methods.append(handle_function(m))
        except:
            print('\tError! Could not generate virtual method %s in interface %s!' % (m.attrib['name'], gir_interface.name))

    for m in find_elements(interface, 'method'):
        try:
            gir_interface.methods.append(handle_function(m))
        except:
            print('\tError! Could not generate method %s in interface %s!' % (m.attrib['name'], gir_interface.name))

    return gir_interface

def handle_property(element_property: ET.Element) -> GirVar | None:
    element_type = find_element(element_property, 'type')
    if element_type is not None and 'name' in element_type.attrib:
        var = GirVar()
        var.name = element_property.attrib['name']
        __handle_type(element_property, var.gtype)
        #var.gtype.name = element_type.attrib['name']
        return var
    return None

def handle_class(element_class: ET.Element) -> GirClass:
    gir_class = GirClass()
    gir_class.name = element_class.attrib['name']

    if 'parent' in element_class.attrib:
        gir_class.implements.append(element_class.attrib['parent'])

    for i in find_elements(element_class, 'implements'):
        gir_class.implements.append(i.attrib['name'])
    
    element_constructor = find_element(element_class, 'constructor')
    if element_constructor is not None:
        try:
            gir_class.constructor = handle_function(element_constructor)
        except:
            print('\tError! Could not generate constructor for class %s!' % gir_class.name)

    for f in find_elements(element_class, 'function'):
        try:
            function = handle_function(f)
            if function is not None:
                gir_class.functions.append(function)
        except:
            print('\tError! Could not generate function %s for class %s!' % (f.attrib['name'], gir_class.name))

    for m in find_elements(element_class, 'method'):
        try:
            method = handle_function(m)
            if method is not None:
                gir_class.methods.append(method)
        except:
            print('\tError! Could not generate method %s for class %s!' % (m.attrib['name'], gir_class.name))

    for p in find_elements(element_class, 'property'):
        prop = handle_property(p)
        if prop is not None:
            gir_class.properties.append(prop)
            
    return gir_class

def handle_enumeration(enumeration: ET.Element) -> GirEnumeration:
    gir_enumeration = GirEnumeration()
    gir_enumeration.name = enumeration.attrib['name']
    for m in find_elements(enumeration, 'member'):
        gir_enumeration.members.append(m.attrib['name'])
    return gir_enumeration

def handle_namespace(namespace: ET.Element, gir: Gir) -> None:
    gir.name = namespace.attrib['name']
    gir.version = namespace.attrib['version']

    for element in find_elements(namespace, 'constant'):
        try:
            c = handle_constant(element)
            if c is not None:
                gir.constants.append(c)
        except:
            print('\tError! Could not generate constant %s!' % element.attrib['name'])

    for element in find_elements(namespace, 'function'):
        try:
            f = handle_function(element)
            if f is not None:
                gir.functions.append(f)
                __handle_function_includes(f, gir)
        except:
            print('\tError! Could not generate function %s!' % element.attrib['name'])

    for element in find_elements(namespace, 'interface'):
        try:
            i = handle_interface(element)
            if i is not None:
                gir.interfaces.append(i)
        except:
            print('\tError! Could not generate interface %s!' % element.attrib['name'])
    
    for element in find_elements(namespace, 'class'):
        try:
            c = handle_class(element)
            if c is not None:
                gir.classes.append(c)
                for f in c.functions:
                    __handle_function_includes(f, gir)
                for m in c.methods:
                    __handle_function_includes(m, gir)
        except:
            print('\tError! Could not generate class %s!' % element.attrib['name'])

    for element in find_elements(namespace, 'bitfield'):
        try:
            e = handle_enumeration(element)
            if e is not None:
                e.is_flag = True
                gir.bitfields.append(e)
        except:
            print('\tError! Could not generate bitfield %s!' % element.attrib['name'])

    for element in find_elements(namespace, 'enumeration'):
        try:
            e = handle_enumeration(element)
            if e is not None:
                gir.enumerations.append(e)
        except:
            print('\tError! Could not generate enumeration %s!' % element.attrib['name'])