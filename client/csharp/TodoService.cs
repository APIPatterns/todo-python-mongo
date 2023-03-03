using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;
using Todo;
using Todo.Models;

// create TodoService as a wrapper for TodoClient
public class TodoService
{
    private readonly TodoClient _client;

    public TodoService()
    {
        var authenticationProvider = new AnonymousAuthenticationProvider();
        var requestAdapter = new HttpClientRequestAdapter(authenticationProvider);
        requestAdapter.BaseUrl = "https://app-api-eao5nur4nxv26.azurewebsites.net";
        _client = new TodoClient(requestAdapter);
    }

    public async Task<IEnumerable<TodoList>?> GetTodoListsAsync()
    {
        var lists = await _client.Lists.GetAsync();
        return lists;
    }

    // Get tasks from selected list
    public async Task<IEnumerable<TodoItem>?> GetTodoItemsAsync(string listId)
    {
        var tasks = await _client.Lists[listId].Items.GetAsync();
        return tasks;
    }

    // Create an item in a list
    public async Task<TodoItem?> CreateTodoItemAsync(string listId,string name, string description)
    {
        var item = new TodoItem
        {
            Name = name,
            Description = description
        };
        var createdItem = await _client.Lists[listId].Items.PostAsync(item);
        return createdItem;
    }
}