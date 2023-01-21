import xml.etree.ElementTree as ET

NAMESPACE = 'http://www.gtk.org/introspection/core/1.0'

def find_element(element: ET.Element, tag: str) -> ET.Element | None:
    return element.find('{%s}%s' % (NAMESPACE, tag))

def find_elements(element: ET.Element, tag: str) -> list[ET.Element]:
    return element.findall('{%s}%s' % (NAMESPACE, tag))

def fix_name(name: str) -> str:
    if name in ('from',):
        return '%s_' % name
    return name

def get_type(type_name: str) -> str:
    if type_name in ('gint','guint','glong','gulong','gint8','guint8','gint16','guint16','gint32','guint32','gint64','guint64','GEnum','GFlags'):
        return 'int'
    elif type_name in ('gfloat', 'gdouble'):
        return 'float'
    elif type_name in ('gchar', 'gchararray', 'utf8'):
        return 'str'
    elif type_name in ('none', 'void'):
        return 'None'
    elif type_name == 'gboolean':
        return 'bool'
    elif type_name == 'GObject':
        return 'GObject.Object'
    elif type_name == 'GInterface':
        return 'GObject.Interface'
    elif type_name == 'GParam':
        return 'GObject.ParamSpec'
    elif type_name == 'GVariant':
        return 'GLib.Variant'
    elif type_name == 'GType':
        return 'GObject.Type'
    elif type_name in ('gpointer', 'GBoxed'):
        return 'object'
    return type_name