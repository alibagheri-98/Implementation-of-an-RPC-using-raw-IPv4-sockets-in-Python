from enum import Enum


class ArgumentType(Enum):
    int_a = 'int'
    str_a = 'str'
    float_a = 'float'
    list_int_a = 'List[int]'
    list_str_a = 'List[str]'
    list_float_a = 'List[float]'

    @staticmethod
    def int_validator(v):
        a = eval(v)
        return isinstance(a, int)

    @staticmethod
    def str_validator(v):
        a = eval(v)
        return isinstance(a, str)

    @staticmethod
    def float_validator(v):
        a = eval(v)
        return isinstance(a, float)

    @staticmethod
    def list_int_validator(v):
        a = eval(v)
        is_list = isinstance(a, list)
        if not is_list:
            return False
        for i in a:
            if i is not int:
                return False
        return True

    @staticmethod
    def list_float_validator(v):
        a = eval(v)
        is_list = isinstance(a, list)
        if not is_list:
            return False
        for i in a:
            if i is not float:
                return False
        return True

    @staticmethod
    def list_str_validator(v):
        a = eval(v)
        is_list = isinstance(a, list)
        if not is_list:
            return False
        for i in a:
            if i is not str:
                return False
        return True

    @staticmethod
    def type_validator(arg_type, arg):
        valid = False
        if arg_type == ArgumentType.int_a.value:
            valid = ArgumentType.int_validator(arg)
        elif arg_type == ArgumentType.float_a.value:
            valid = ArgumentType.float_validator(arg)
        elif arg_type == ArgumentType.str_a.value:
            valid = ArgumentType.str_validator(arg)
        elif arg_type == ArgumentType.list_int_a.value:
            valid = ArgumentType.list_int_validator(arg)
        elif arg_type == ArgumentType.list_float_a.value:
            valid = ArgumentType.list_float_validator(arg)
        elif arg_type == ArgumentType.list_str_a.value:
            valid = ArgumentType.list_str_validator(arg)
        return valid


class RPCExceptionTypes(Enum):
    ExecutionException = 'ExecutionException'
    InvalidArguments = 'InvalidArguments'
    ServiceNotFound = 'ServiceNotFound'
    RPCNotFound = 'RPCNotFound'
    ClientNotRegistered = 'ClientNotRegistered'
