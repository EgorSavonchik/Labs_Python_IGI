import inspect
from Serializers import nonetype, moduletype, codetype, celltype, \
                          functype, bldinfunctype, \
                          mapproxytype, wrapdesctype, metdesctype, getsetdesctype, \
                          CODE_PROPS, UNIQUE_TYPES

class DictSerializer:
    TYPE_KW = "type"
    SOURCE_KW = "source"

    CODE_KW = "__code__"
    GLOBALS_KW = functype.__globals__.__name__
    NAME_KW = "__name__"
    DEFAULTS_KW = "__defaults__"
    CLOSURE_KW = functype.__closure__.__name__

    BASES_KW = "__bases__"
    DICT_KW = "__dict__"

    CLASS_KW = "__class__"

    OBJECT_KW = "object"

    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, nonetype):
            return obj

        if type(obj) is list:
            return [cls.to_dict(o) for o in obj]

        if type(obj) is dict:
            # Since the key in the dictionary can be a hashable object, which will be represented as a non-hashable
            # dictionary, it is easier to represent the dictionary as a list of key-value pairs
            return {cls.TYPE_KW: dict.__name__,
                    cls.SOURCE_KW: [[cls.to_dict(item[0]), cls.to_dict(item[1])] for item in obj.items()]}

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            return {cls.TYPE_KW: type(obj).__name__,
                    cls.SOURCE_KW: cls.to_dict([*obj])}

        if type(obj) is complex:
            return {cls.TYPE_KW: complex.__name__,
                    cls.SOURCE_KW: {complex.real.__name__: obj.real,
                                    complex.imag.__name__: obj.imag}}

        if type(obj) is moduletype:
            return {cls.TYPE_KW: moduletype.__name__,
                    cls.SOURCE_KW: obj.__name__}

        if type(obj) is codetype:
            code = {cls.TYPE_KW: codetype.__name__}
            source = {}

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_PROPS:
                    source[key] = cls.to_dict(value)

            code.update({cls.SOURCE_KW: source})
            return code

        if type(obj) is celltype:
            return {cls.TYPE_KW: celltype.__name__,
                    cls.SOURCE_KW: cls.to_dict(obj.cell_contents)}

        if type(obj) in (staticmethod, classmethod):
            return {cls.TYPE_KW: type(obj).__name__,
                cls.SOURCE_KW: cls.to_dict(obj.__func__, is_inner_func)}

        if inspect.isroutine(obj):
            source = {}

            # Code
            source[cls.CODE_KW] = cls.to_dict(obj.__code__)

            # Global vars
            gvars = cls.__get_gvars(obj, is_inner_func)
            source[cls.GLOBALS_KW] = cls.to_dict(gvars)

            # Name
            source[cls.NAME_KW] = cls.to_dict(obj.__name__)

            # Defaults
            source[cls.DEFAULTS_KW] = cls.to_dict(obj.__defaults__)

            # Closure
            source[cls.CLOSURE_KW] = cls.to_dict(obj.__closure__)

            return {cls.TYPE_KW: functype.__name__,
                    cls.SOURCE_KW: source}

        elif inspect.isclass(obj):
            source = {}

            # Name
            source[cls.NAME_KW] = cls.to_dict(obj.__name__)

            # Bases
            source[cls.BASES_KW] = cls.to_dict(tuple(b for b in obj.__bases__ if b != object))

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: type.__name__,
                    cls.SOURCE_KW: source}

        else:
            source = {}

            # Class
            source[cls.CLASS_KW] = cls.to_dict(obj.__class__)

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: cls.OBJECT_KW,
                    cls.SOURCE_KW: source}

    @classmethod
    def __get_gvars(cls, func, is_inner_func):
        name = func.__name__
        gvars = {}

        for gvar_name in func.__code__.co_names:
            # Separating the variables that the function needs
            if gvar_name in func.__globals__:

                # Module
                if type(func.__globals__[gvar_name]) is moduletype:
                    gvars[gvar_name] = func.__globals__[gvar_name]

                # Class
                elif inspect.isclass(func.__globals__[gvar_name]):
                    # To prevent recursion, the class in which this method is declared is replaced with the
                    # name of the class. In the future, this name will be replaced by the class type
                    c = func.__globals__[gvar_name]
                    if is_inner_func and name in c.__dict__ and func == c.__dict__[name].__func__: #!!!!
                        gvars[gvar_name] = c.__name__
                    else:
                        gvars[gvar_name] = c

                # Recursion protection
                elif gvar_name == func.__code__.co_name:
                    gvars[gvar_name] = func.__name__

                else:
                    gvars[gvar_name] = func.__globals__[gvar_name]

        return gvars

    @classmethod
    def __get_obj_dict(cls, obj):
        dct = {item[0]: item[1] for item in obj.__dict__.items()}
        dct2 = {}

        for key, value in dct.items():
            if type(value) not in UNIQUE_TYPES:
                if inspect.isroutine(value):
                    # Recursion protection
                    dct2[cls.to_dict(key)] = cls.to_dict(value, is_inner_func=True)
                else:
                    dct2[cls.to_dict(key)] = cls.to_dict(value)

        return dct2

    @classmethod
    def from_dict(cls, obj, is_dict=False):

        if is_dict:
            return {cls.from_dict(item[0]): cls.from_dict(item[1]) for item in obj}

        if type(obj) not in (dict, list):
            return obj

        elif type(obj) is list:
            return [cls.from_dict(o) for o in obj]

        else:
            obj_type = obj[cls.TYPE_KW]
            obj_source = obj[cls.SOURCE_KW]

            if obj_type == dict.__name__:
                return cls.from_dict(obj_source, is_dict=True)

            # Key - type name, value - type itself. Calling by type name returns that type.
            # This is necessary for the same creation of simple collections.
            cols_dict = {t.__name__: t for t in [set, frozenset, tuple, bytes, bytearray]}
            if obj_type in cols_dict:
                return cols_dict[obj_type](cls.from_dict(obj_source))

            if obj_type == complex.__name__:
                return obj_source[complex.real.__name__] + \
                    obj_source[complex.imag.__name__] * 1j

            if obj_type == moduletype.__name__:
                return __import__(obj_source)

            if obj_type == codetype.__name__:
                return codetype(*[cls.from_dict(obj_source[prop]) for prop in CODE_PROPS])

            if obj_type == celltype.__name__:
                return celltype(cls.from_dict(obj_source))

            if obj_type == staticmethod.__name__:
                return staticmethod(cls.from_dict(obj_source))

            if obj_type == classmethod.__name__:
                return classmethod(cls.from_dict(obj_source))

            if obj_type == functype.__name__:
                code = cls.from_dict(obj_source[cls.CODE_KW])
                gvars = cls.from_dict(obj_source[cls.GLOBALS_KW])
                name = cls.from_dict(obj_source[cls.NAME_KW])
                defaults = cls.from_dict(obj_source[cls.DEFAULTS_KW])
                closure = cls.from_dict(obj_source[cls.CLOSURE_KW])

                # If there are suitable global variables, they are replaced.
                for key in gvars:
                    if key in code.co_name and key in globals():
                        gvars[key] = globals()[key]

                func = functype(code, gvars, name, defaults, closure)

                # Restoring recursion
                if func.__name__ in gvars:
                    func.__globals__.update({func.__name__: func})

                return func

            if obj_type == type.__name__:
                name = cls.from_dict(obj_source[cls.NAME_KW])
                bases = cls.from_dict(obj_source[cls.BASES_KW])
                dct = obj_source[cls.DICT_KW]
                dct = {cls.from_dict(item[0]): cls.from_dict(item[1]) for item in dct.items()}

                cl = type(name, bases, dct)

                # Restore a reference to the current class in the nested method __globals__
                for attr in cl.__dict__.values():
                    if inspect.isroutine(attr):
                        if type(attr) in (staticmethod, classmethod):
                            fglobs = attr.__func__.__globals__
                        else:
                            fglobs = attr.__globals__

                        for gv in fglobs.keys():
                            if gv == cl.__name__:
                                fglobs[gv] = cl

                return cl

            else:
                clas = cls.from_dict(obj_source[cls.CLASS_KW])
                dct = obj_source[cls.DICT_KW]
                dct = {cls.from_dict(item[0]): cls.from_dict(item[1]) for item in dct.items()}

                o = object.__new__(clas)
                o.__dict__ = dct

                return o






