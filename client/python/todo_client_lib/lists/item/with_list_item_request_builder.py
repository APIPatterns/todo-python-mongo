from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

items_request_builder = lazy_import('todo_client_lib.lists.item.items.items_request_builder')
with_item_item_request_builder = lazy_import('todo_client_lib.lists.item.items.item.with_item_item_request_builder')
todo_list = lazy_import('todo_client_lib.models.todo_list')

class WithListItemRequestBuilder():
    """
    Builds and executes requests for operations under /lists/{listId}
    """
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        The items property
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WithListItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/lists/{listId}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WithListItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a Todo list by unique identifier
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, None)
    
    async def get(self,request_configuration: Optional[WithListItemRequestBuilderGetRequestConfiguration] = None) -> Optional[todo_list.TodoList]:
        """
        Gets a Todo list by unique identifier
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[todo_list.TodoList]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, todo_list.TodoList, None)
    
    def items_by_id(self,id: str) -> with_item_item_request_builder.WithItemItemRequestBuilder:
        """
        Gets an item from the todo_client_lib.lists.item.items.item collection
        Args:
            id: Unique identifier of the item
        Returns: with_item_item_request_builder.WithItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemId"] = id
        return with_item_item_request_builder.WithItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def put(self,body: Optional[todo_list.TodoList] = None, request_configuration: Optional[WithListItemRequestBuilderPutRequestConfiguration] = None) -> Optional[todo_list.TodoList]:
        """
        Updates a Todo list by unique identifier
        Args:
            body:  A list of related Todo items
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[todo_list.TodoList]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, todo_list.TodoList, None)
    
    def to_delete_request_information(self,request_configuration: Optional[WithListItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a Todo list by unique identifier
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[WithListItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Gets a Todo list by unique identifier
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_put_request_information(self,body: Optional[todo_list.TodoList] = None, request_configuration: Optional[WithListItemRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Updates a Todo list by unique identifier
        Args:
            body:  A list of related Todo items
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class WithListItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WithListItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WithListItemRequestBuilderPutRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

