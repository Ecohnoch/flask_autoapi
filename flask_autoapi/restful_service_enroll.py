# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : restful_service_enroll.py
# @Function : TODO

import os
import sys

import traceback
from flask import Flask, request
import flask_restful as restful

from .exceptions import ConfigException, ServiceInterfaceException, OutPutParamsNotMatchException

class RestfulServiceEnroll(object):
    def __init__(self, config, app=None, api=None):
        self.config = config
        self._check_config()

        if app is None and api is None:
            self.app, self.api = self.init_app()
        self._get_service_interface()
        self._api_class_register()


    def _check_config(self):
        keys = self.config.keys()
        check_keys = ['service_dir', 'service_python_filename', 'service_python_interface', 'service_input_params', 'service_output_params', 'deploy_mode', 'deploy_port', 'service_route']
        if len(keys) != len(check_keys):
            raise ConfigException(
                'Config Error, given config keys: {}, but need {}'.format(keys, check_keys))
        for each_key, each_check_key in zip(keys, check_keys):
            if each_key != each_check_key:
                raise ConfigException(
                    'Config Error, key name error, given {}, but need {}: '.format(each_key, each_check_key))

        if not os.path.exists(self.config['service_dir']):
            raise ConfigException(
                'Config Error, service dir not existed: {}'.format(self.config['service_dir']))
        if self.config['service_python_filename']+'.py' not in os.listdir(self.config['service_dir']):
            raise ConfigException(
                'Config Error, service file {} not in service dir: {}'.format(self.config['service_python_filename'], self.config['service_dir']))
        if '__init__.py' not in os.listdir(self.config['service_dir']):
            print('Config Warning, service file {} not in service dir: {}'.format('__init__.py', self.config['service_dir']))

        self.absolute_service_dir = os.path.abspath(self.config['service_dir'])


    def _get_service_interface(self):
        sys.path.append(self.absolute_service_dir)
        import importlib
        service_module = importlib.import_module(self.config['service_python_filename'])
        if not hasattr(service_module, self.config['service_python_interface']):
            raise ServiceInterfaceException('Service python file {} has no interface: {} '.format(
                self.config['service_python_filename'],
                self.config['service_python_interface']
            ))

        self.service_interface = getattr(service_module, self.config['service_python_interface'])


    def _api_class_register(self):
        global_config = self.config
        service_interface = self.service_interface
        class API(restful.Resource):
            def __init__(self):
                super(API, self).__init__()
                self.config = global_config
                self.service_interface = service_interface
            def get(self):
                try:
                    service_input_params  = self.config['service_input_params']
                    service_output_params = self.config['service_output_params']

                    input_params = []
                    for each_service_input in service_input_params:
                        input_params.append(request.args.get(each_service_input))
                    current_work_dir_path = os.path.abspath(os.getcwd())
                    os.chdir(self.absolute_service_dir)
                    return_results = self.service_interface(*input_params)
                    os.chdir(current_work_dir_path)
                    if len(service_output_params) == 0:
                        return {'status': 200}
                    if len(service_output_params) == 1 and isinstance(return_results, tuple):
                        raise OutPutParamsNotMatchException('Service output params only has 1 but return results has many.')
                    if len(service_output_params) == 1:
                        param_name = service_output_params[list(service_output_params.keys())[0]]
                        return {'status': 200, param_name: return_results}
                    if len(service_output_params) > 1 and isinstance(return_results, tuple) and len(return_results) == len(service_output_params):
                        ans = {'status': 200}
                        for each_key, each_result in zip(service_output_params, return_results):
                            ans[each_key] = each_result
                        return ans
                    raise OutPutParamsNotMatchException('Service output params and return results are not match, return result: {}'.format(return_results))
                except Exception as e:
                    traceback.print_exc()
                    return {'status': 400, 'err_msg': str(e)}
        self.registered_api = API
        self.api.add_resource(API, self.config['service_route'])

    def init_app(self):
        app = Flask(__name__)
        api = restful.Api(app)
        return app, api

    def launch_app(self, host=None):
        if host is None:
            self.app.run(port=self.config['deploy_port'])
        else:
            self.app.run(host=host, port=self.config['deploy_port'])



