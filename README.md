# Flask-autoapi

This project is mainly for machine learning projects. Sometimes a machine learning service is written, but it requires a lot of additional code to deploy. Is there any way to register a service to restful api for deployment without changing all the code of the machine learning service? flask-autoapi gives the answer.

First, you need to put the entire code of your machine learning service into a directory to become a module (actually add the \_\_init\_\_.py file in this directory), and then specify which python file in the directory contains Service, and then specify which function of this file provides the service. Turn the above into a config and directly call flask_autoapi.launch(config) to deploy the service directly.


### Download

```
pip install flask-auto-api -i https://pypi.python.org/simple
```

### Describe

You only need a test function that you can run locally (no matter where the function is) and a configuration to start the api service.

The configuration dictionary needs to contain the following options:

1. service_dir: the folder where the service is located.
2. service_python_filename: the python file name where the service is located. (filename.py, don't add .py)
3. service_python_interface: the service interface name.
4. service_input_params: it is a dict, the keys must be same as the names of input interface params, the values are describes.
5. deploy_mode: now only provide 'restful'.
6. deploy_port: api port, check the port is not occupied.
7. service_route: api route.


### Example

Step1: Suppose you have a local service named service2, and you want to provide service2.service as a restful service.

Step2: Make the service2 directory as a python module first.

The example service2 may have its own dependcies, not worry, you don't need to change any codes.

services/service2/service2：

```
from dependencies import add, mul

def service2(param1, param2, param3):
    param1 = int(param1)
    param2 = int(param2)
    param3 = int(param3)

    ans1 = add(param1, param2, param3)
    ans2 = mul(param1, param2, param3)

    return str(ans1), str(ans2)
```

It should be noted that the input parameters and output parameters of the interface functions that provide services must be in the type of strings, of course, there is no limit to the parameter number.


Step3: Make such a config dictionary:

```python
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
```

It should be noted that the input and output parameters of the interface must be written in the configuration dict in the same form, and the keys of service_input_params or service_output_params will be the http request parameter and the response keys respectively. The values of service_input_params and service_output_params are describes to those parameters.

Step4: Then launch this service api:

```python
import flask_autoapi
flask_autoapi.launch(service_config)
```

Step5: The service will be running:

```
 * Running on http://127.0.0.1:12345/ (Press CTRL+C to quit)
 * Serving Flask app "flask_autoapi.restful_service_enroll" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
```

The test url:

```
http://127.0.0.1:12345/test_service?param1=1&param2=2&param3=3
```

The response:

```
{"status": 200, "add_result": "6", "mul_result": "6"}
```


### Dependencies

```
flask-1.1.2
flask-RESTFUL-0.3.8
```
