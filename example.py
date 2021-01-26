# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : main.py
# @Function : TODO

import flask_autoapi

service_config = {
    'service_dir'               : './services/service2', # Service root directory
    'service_python_filename'   : 'service2',            # service2.py
    'service_python_interface'  : 'service2',            # service2 is the interface function

    'service_input_params' : {                           # interface input params are defined here
        'param1': 'param1 describe here',
        'param2': 'param2 describe here',
        'param3': 'param3 describe here',
    },

    'service_output_params' : {                          # interface output params are defined here
        'add_result': 'value describe here',
        'mul_result': 'value describe here'
    },

    'deploy_mode'   : 'restful', # c++ deploy            # now only has restful deploy
    'deploy_port'   : '12345',                           # service port
    'service_route' : '/test_service'                    # service route
}



if __name__ == '__main__':
    flask_autoapi.launch(service_config)