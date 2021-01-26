# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : main.py
# @Function : TODO

import flask_autoapi

service2_config = {
    'service_dir'               : './services/service2',
    'service_python_filename'   : 'service2',
    'service_python_interface'  : 'service2',

    'service_input_params' : {
        'param1': 'param1',
        'param2': 'param2',
        'param3': 'param3',
    },

    'service_output_params' : {
        'value': 'value'
    },

    'deploy_mode'   : 'restful', # c++ deploy
    'deploy_port'   : '12345',
    'service_route' : '/test_service'
}



if __name__ == '__main__':
    flask_autoapi.launch(service2_config)