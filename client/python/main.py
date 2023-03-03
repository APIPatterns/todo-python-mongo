import asyncio
from todo_service import TodoService

async def main():

    service = TodoService()

    lists = await service.get_todo_lists()

    # print the names of the lists
    for list in lists:
        print(list.name)
        # Print items in the list
        items = await service.get_todo_items(list.id)
        for item in items:
            print(item.description)

asyncio.run(main())