# Flask-autoapi

This project is mainly for machine learning projects. Sometimes a machine learning service is written, but it requires a lot of additional code to deploy. Is there any way to register a service to restful api for deployment without changing all the code of the machine learning service? flask-autoapi gives the answer.

First, you need to put the entire code of your machine learning service into a directory to become a module (actually add the \_\_init\_\_.py file in this directory), and then specify which python file in the directory contains Service, and then specify which function of this file provides the service. Turn the above into a config and directly call flask_autoapi.launch(config) to deploy the service directly.


### Dependencies

```
flask-1.1.2
flask-RESTFUL-0.3.8
```


# Example

Step1: Suppose you have a local service named service2, and you want to provide service2.service as a restful service.

Step2: Make the service2 directory as a python module first.

The example service2 may have its own dependcies, not worry, you don't need to change any codes.

services/service2/service2：

```
import dependencies

def service2(param1, param2, param3):
    param1 = int(param1)
    param2 = int(param2)
    param3 = int(param3)
    ans = param1 + param2 + param3
    print(ans, str(ans))
    return str(ans)
```

It should be noted that the input parameters and output parameters of the interface functions that provide services must be in the type of strings, of course, there is no limit to the parameter number.


Step3: Make such a config dictionary:

```python
service_config = {
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
```

It should be noted that the input and output parameters of the interface must be written in the configuration dict in the same form, and the keys of service_input_params or service_output_params will be the http request parameter and the response keys respectively. The values of service_input_params and service_output_params are describes to those parameters.

Step4: Then launch this service api:

```python
import flask_autoapi
flask_autoapi.launch(service_config)
```

Step5: The service will be running:

test url:

```
http://127.0.0.1:12345/test_service?param1=1&param2=2&param3=3
```
