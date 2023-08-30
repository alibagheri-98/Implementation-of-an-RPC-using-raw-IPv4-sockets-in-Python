import importlib.util
import sys
from inspect import getmembers, isfunction


def load_module_from_script_file(path_to_file, file_name):
    spec = importlib.util.spec_from_file_location(file_name, path_to_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[file_name] = module
    spec.loader.exec_module(module)
    return getmembers(module, isfunction)[0][1]
