from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ....models import todo_item
from .state import state_request_builder
from .state.item import with_state_item_request_builder

class ItemsRequestBuilder():
    """
    Builds and executes requests for operations under /lists/{listId}/items
    """
    def state(self) -> state_request_builder.StateRequestBuilder:
        """
        The state property
        """
        return state_request_builder.StateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ItemsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/lists/{listId}/items{?top*,skip*}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[ItemsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Gets Todo items within the specified list
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_post_request_information(self,body: Optional[todo_item.TodoItem] = None, request_configuration: Optional[ItemsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Creates a new Todo item within a list
        Args:
            body: A task that needs to be completed
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[ItemsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[List[todo_item.TodoItem]]:
        """
        Gets Todo items within the specified list
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[List[todo_item.TodoItem]]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_collection_async(todo_item.TodoItem)(request_info, todo_item.TodoItem, response_handler, None)
    
    async def post(self,body: Optional[todo_item.TodoItem] = None, request_configuration: Optional[ItemsRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[todo_item.TodoItem]:
        """
        Creates a new Todo item within a list
        Args:
            body: A task that needs to be completed
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[todo_item.TodoItem]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, todo_item.TodoItem, response_handler, None)
    
    def state_by_id(self,id: str) -> with_state_item_request_builder.WithStateItemRequestBuilder:
        """
        Gets an item from the ApiSdk.lists.item.items.state.item collection
        Args:
            id: Unique identifier of the item
        Returns: with_state_item_request_builder.WithStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["state"] = id
        return with_state_item_request_builder.WithStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ItemsRequestBuilderGetQueryParameters():
        """
        Gets Todo items within the specified list
        """
        # The number of items to skip within the results
        skip: Optional[str] = None

        # The max number of items to returns in a result
        top: Optional[str] = None

    
    @dataclass
    class ItemsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ItemsRequestBuilder.ItemsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ItemsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

