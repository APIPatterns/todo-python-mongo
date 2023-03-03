// Create TodoService, get lists and print them
var todoService = new TodoService();
var lists = await todoService.GetTodoListsAsync();
foreach (var list in lists)
{
    Console.WriteLine(list.Name);
    // Add Item to list
    var item = await todoService.CreateTodoItemAsync(list.Id, "Work", "Work on Kiota in CSharp");


    // Get tasks from selected list
    var tasks = await todoService.GetTodoItemsAsync(list.Id);
    foreach (var task in tasks)
    {
        Console.WriteLine($"\t{task.Description}");
    }
}