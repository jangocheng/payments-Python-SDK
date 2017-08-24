# coding: utf-8

"""
    Mpesa  Service

    This is an internal Mpesa Service that communicates via REST to the Safaricom Daraja API

    OpenAPI spec version: 1.0
    Contact: ondengew@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class B2cApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def b2c_create(self, authorization, x_account, payload, **kwargs):
        """
        create b2c
        creates a b2c payment request
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.b2c_create(authorization, x_account, payload, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: (required)
        :param int x_account: (required)
        :param B2CPayload1 payload: Use this API to transact between an M-Pesa short code to a phone number registered on M-Pesa. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.b2c_create_with_http_info(authorization, x_account, payload, **kwargs)
        else:
            (data) = self.b2c_create_with_http_info(authorization, x_account, payload, **kwargs)
            return data

    def b2c_create_with_http_info(self, authorization, x_account, payload, **kwargs):
        """
        create b2c
        creates a b2c payment request
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.b2c_create_with_http_info(authorization, x_account, payload, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: (required)
        :param int x_account: (required)
        :param B2CPayload1 payload: Use this API to transact between an M-Pesa short code to a phone number registered on M-Pesa. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_account', 'payload']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method b2c_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `b2c_create`")
        # verify the required parameter 'x_account' is set
        if ('x_account' not in params) or (params['x_account'] is None):
            raise ValueError("Missing the required parameter `x_account` when calling `b2c_create`")
        # verify the required parameter 'payload' is set
        if ('payload' not in params) or (params['payload'] is None):
            raise ValueError("Missing the required parameter `payload` when calling `b2c_create`")

        if 'x_account' in params and params['x_account'] < 1:
            raise ValueError("Invalid value for parameter `x_account` when calling `b2c_create`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_account' in params:
            header_params['X-Account'] = params['x_account']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/b2c/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)