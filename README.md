# Flask-autoapi




# Example

Step1: Suppose you have a local service named service2, and you make it as a python module first.

Step2: Make such a config dictionary:

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

Step3: Then launch this service api:

```python
import flask_autoapi
flask_autoapi.launch(service_config)
```

Step4: The service will be running:

test url:

```
http://127.0.0.1:12345/test_service?param1=1&param2=2&param3=3
```
