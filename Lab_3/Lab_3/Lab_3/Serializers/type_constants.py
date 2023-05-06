import types
from types import NoneType as nonetype, \
                  ModuleType as moduletype, \
                  CodeType as codetype, \
                  FunctionType as functype, \
                  BuiltinFunctionType as bldinfunctype, \
                  CellType as celltype, \
                  MappingProxyType as mapproxytype, \
                  WrapperDescriptorType as wrapdesctype, \
                  MethodDescriptorType as metdesctype, \
                  GetSetDescriptorType as getsetdesctype

CODE_PROPS = [prop.__name__ for prop in [
        codetype.co_argcount,
        codetype.co_posonlyargcount,
        codetype.co_kwonlyargcount,
        codetype.co_nlocals,
        codetype.co_stacksize,
        codetype.co_flags,
        codetype.co_code,
        codetype.co_consts,
        codetype.co_names,
        codetype.co_varnames,
        codetype.co_filename,
        codetype.co_name,
       # codetype.co_qualname,
        codetype.co_firstlineno,
        codetype.co_lnotab,
     #   codetype.co_exceptiontable,
        codetype.co_freevars,
        codetype.co_cellvars]
    ]

UNIQUE_TYPES = [
    mapproxytype,
    wrapdesctype,
    metdesctype,
    getsetdesctype,
    bldinfunctype
]
