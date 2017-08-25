# swagger_client.AccountApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_create**](AccountApi.md#account_create) | **POST** /v1/accounts | create account
[**account_delete**](AccountApi.md#account_delete) | **DELETE** /v1/accounts/{accountID} | delete account
[**account_list**](AccountApi.md#account_list) | **GET** /v1/accounts | list account
[**account_show**](AccountApi.md#account_show) | **GET** /v1/accounts/{accountID} | show account
[**account_update**](AccountApi.md#account_update) | **PUT** /v1/accounts/{accountID} | update account


# **account_create**
> account_create(payload)

create account

Create new account

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
payload = swagger_client.CreateAccountPayload1() # CreateAccountPayload1 | 

try: 
    # create account
    api_instance.account_create(payload)
except ApiException as e:
    print("Exception when calling AccountApi->account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateAccountPayload1**](CreateAccountPayload1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_delete**
> account_delete(account_id)

delete account

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account_id = 56 # int | Account ID

try: 
    # delete account
    api_instance.account_delete(account_id)
except ApiException as e:
    print("Exception when calling AccountApi->account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_list**
> list[MediatypeIdentifierApplicationvndAccountjsonViewdefault] account_list()

list account

Retrieve all accounts.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()

try: 
    # list account
    api_response = api_instance.account_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MediatypeIdentifierApplicationvndAccountjsonViewdefault]**](MediatypeIdentifierApplicationvndAccountjsonViewdefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.account+json; type=collection

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_show**
> MediatypeIdentifierApplicationvndAccountjsonViewdefault account_show(account_id)

show account

Retrieve account with given id. IDs 1 and 2 pre-exist in the system.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account_id = 56 # int | Account ID

try: 
    # show account
    api_response = api_instance.account_show(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 

### Return type

[**MediatypeIdentifierApplicationvndAccountjsonViewdefault**](MediatypeIdentifierApplicationvndAccountjsonViewdefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error, application/vnd.account+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_update**
> account_update(account_id, payload)

update account

Change account name

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account_id = 56 # int | Account ID
payload = swagger_client.UpdateAccountPayload1() # UpdateAccountPayload1 | 

try: 
    # update account
    api_instance.account_update(account_id, payload)
except ApiException as e:
    print("Exception when calling AccountApi->account_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **payload** | [**UpdateAccountPayload1**](UpdateAccountPayload1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

