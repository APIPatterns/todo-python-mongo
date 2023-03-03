
from typing import List
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_abstractions.authentication.anonymous_authentication_provider import AnonymousAuthenticationProvider
from todo_client_lib.models.todo_item import TodoItem
from todo_client_lib.todo_client import TodoClient
from todo_client_lib.models.todo_list import TodoList

class TodoService():
    def __init__(self):
        provider = AnonymousAuthenticationProvider()
        request_adapter = HttpxRequestAdapter(provider)
        request_adapter.base_url = "https://app-api-eao5nur4nxv26.azurewebsites.net"
        self.client = TodoClient(request_adapter)
        

    async def get_todo_lists(self) -> List[TodoList]:
        lists = await self.client.lists.get()
        return lists
    
    """get todo list by id"""
    async def get_todo_list_by_id(self, id: str) -> TodoList:
        list = await self.client.lists_by_id(id).get()
        return list

    """Get Todo Items from a list"""
    async def get_todo_items(self, list_id: str) -> List[TodoItem]:
        items = await self.client.lists_by_id(list_id).items.get()
        return items
