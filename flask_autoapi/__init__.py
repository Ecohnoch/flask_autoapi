# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : __init__.py.py
# @Function : TODO

from .restful_service_enroll import RestfulServiceEnroll

def save_service(config, save_path):
    service_object = RestfulServiceEnroll(config=config)
    import pickle
    with open(save_path, 'wb') as f:
        pickle.dump(service_object.app, f)

def launch(config):
    service_object = RestfulServiceEnroll(config=config)
    service_object.launch_app()
