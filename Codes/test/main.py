import importlib.util
import sys
from inspect import getmembers, isfunction

file_name = "rpc2"
module_name = "rpc2"
path_to_file = "E:\\Documentwork\\sharif\\rasoul stuff\\RPC project\\test\\rpc2.py"

spec = importlib.util.spec_from_file_location(file_name, location=path_to_file)
module = importlib.util.module_from_spec(spec)
sys.modules[file_name] = module
spec.loader.exec_module(module)
print(getmembers(module, isfunction))
