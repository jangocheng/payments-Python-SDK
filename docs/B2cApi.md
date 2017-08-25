# swagger_client.B2cApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**b2c_create**](B2cApi.md#b2c_create) | **POST** /v1/b2c/ | create b2c


# **b2c_create**
> b2c_create(payload)

create b2c

creates a b2c payment request

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.B2cApi()
payload = swagger_client.B2CPayload1() # B2CPayload1 | Use this API to transact between an M-Pesa short code to a phone number registered on M-Pesa.

try: 
    # create b2c
    api_instance.b2c_create(payload)
except ApiException as e:
    print("Exception when calling B2cApi->b2c_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**B2CPayload1**](B2CPayload1.md)| Use this API to transact between an M-Pesa short code to a phone number registered on M-Pesa. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

