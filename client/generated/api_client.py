from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, Union

from .lists import lists_request_builder
from .lists.item import with_list_item_request_builder

class ApiClient():
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def lists(self) -> lists_request_builder.ListsRequestBuilder:
        """
        The lists property
        """
        return lists_request_builder.ListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new ApiClient and sets the default values.
        Args:
            requestAdapter: The request adapter to use to execute the requests.
        """
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Path parameters for the request
        self.path_parameters: Dict[str, Any] = {}

        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}"

        self.request_adapter = request_adapter
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
    
    def lists_by_id(self,id: str) -> with_list_item_request_builder.WithListItemRequestBuilder:
        """
        Gets an item from the ApiSdk.lists.item collection
        Args:
            id: Unique identifier of the item
        Returns: with_list_item_request_builder.WithListItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listId"] = id
        return with_list_item_request_builder.WithListItemRequestBuilder(self.request_adapter, url_tpl_params)
    

