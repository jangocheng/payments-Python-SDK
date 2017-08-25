# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**js_js_filepath**](DefaultApi.md#js_js_filepath) | **GET** /js/{filepath} | Download public/js
[**public_ui**](DefaultApi.md#public_ui) | **GET** /ui | Download public/html/index.html
[**swagger_swagger_json**](DefaultApi.md#swagger_swagger_json) | **GET** /swagger.json | Download public/swagger/swagger.json


# **js_js_filepath**
> file js_js_filepath(filepath)

Download public/js

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
filepath = 'filepath_example' # str | Relative file path

try: 
    # Download public/js
    api_response = api_instance.js_js_filepath(filepath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->js_js_filepath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepath** | **str**| Relative file path | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_ui**
> file public_ui()

Download public/html/index.html

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Download public/html/index.html
    api_response = api_instance.public_ui()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->public_ui: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swagger_swagger_json**
> file swagger_swagger_json()

Download public/swagger/swagger.json

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Download public/swagger/swagger.json
    api_response = api_instance.swagger_swagger_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->swagger_swagger_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

