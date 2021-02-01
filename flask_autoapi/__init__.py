# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : __init__.py.py
# @Function : TODO

from .restful_service_enroll import RestfulServiceEnroll

def register(config):
    service_object = RestfulServiceEnroll(config=config)
    return service_object.app, service_object.api

def register_with_app(config, app, api):
    service_object = RestfulServiceEnroll(config=config, app=app, api=api)
    return service_object.app, service_object.api

def launch(config, host=None):
    service_object = RestfulServiceEnroll(config=config)
    service_object.launch_app(host)
