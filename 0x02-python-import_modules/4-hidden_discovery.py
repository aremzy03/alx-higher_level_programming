#!/usr/bin/python3
import importlib
module_name = "hidden_4"
path = "hidden_4.pyc"

spec = importlib.util.spec_from_file_location(module_name, path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
dir(module_name)
