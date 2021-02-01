# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : __init__.py.py
# @Function : TODO

class ConfigException(Exception):
    def __init__(self, err_msg):
        Exception.__init__(self, err_msg)

class ServiceInterfaceException(Exception):
    def __init__(self, err_msg):
        Exception.__init__(self, err_msg)


class OutPutParamsNotMatchException(Exception):
    def __init__(self, err_msg):
        Exception.__init__(self, err_msg)