"""
    pyexcel._compact
    ~~~~~~~~~~~~~~~~~~~

    Compatibles

    :copyright: (c) 2014 by C. W.
    :license: GPL v3
"""
import sys


if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

PY2 = sys.version_info[0] == 2
    
if PY2:
    from StringIO import StringIO
    text_type = unicode
    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')
    class Iterator(object):
        def next(self):
            return type(self).__next__(self)
else:
    from io import StringIO
    text_type = str
    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value
    Iterator = object


def is_array_type(an_array, atype):
    tmp = [i for i in an_array if not isinstance(i, atype)]
    return len(tmp) == 0


def is_string(atype):
    """find out if a type is str or not"""
    if atype == str:
            return True
    elif PY2:
        if atype == unicode:
            return True
    return False
