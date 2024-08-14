def add_task(task_list):
    name = input("enter your task: ")
    task_list.append(name)
    return task_list

def update_task(task_list):
        task_number = int(input("enter your task no. ")) - 1
        if 0 <= task_number < len(task_list):
             name = input("Enter your updated task: ")
             task_list[task_number] = name
        else : 
            print("task not found")

def delete_task(task_list):
     
     task_number = int(input("enter your task no. ")) - 1
     if 0 <= task_number < len(task_list):
         task_list.pop(task_number)
     else:
         print("task not found") 
        

def show_all_task(task_list):
      for i, task in enumerate(task_list, start=1):
            if not task in task_list:
                print("task not found")
            else:
                print(f"{i}. {task}")



def main():
    task_list = []
    while True:


        print("1. Add task ")
        print("2. Update a task ")
        print("3. Delete a task ")
        print("4. show all tasks ")
        print("5. Exit")

        choice = input("ENter your choice: ")

        if choice == '1':
            add_task(task_list)

        if choice == '2': 
            update_task(task_list)

        if choice == '3':
            delete_task(task_list) 
        
        if choice == '4':
            show_all_task(task_list)


        if choice == '5':
            break

if __name__ == "__main__":
    main()
