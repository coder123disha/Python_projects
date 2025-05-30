#Create  an empty list  to store the tasks  and their  status

todo_list=[]

#func to add new task
def add_task():
    task=input("Enter Your NEW TASK=")
    todo_list.append({"Task":task,"Status":"Pending"})
    print("Your task is successfully uploaded \n")

#func to view all tasks
def view_task():
    print("All the tasks in the list")
    #we will check if our list is empty or not 
    if len(todo_list)==0:
        print("YOU HAVE ZERO TASKS IN YOUR TO DO LIST")
    else:
        for index,val in enumerate(todo_list,1):
            print(f"{index}:{val['Task']}-{val['Status']}")
    print("\n")

#func to remove the task from the to do list
def remove_task():
    #check if the list is not empty
    if len(todo_list)==0:
        print("LIST IS EMPTY")
    else:
        try:
            search_index=int(input("Enter the task index you want to remove"))-1;
            if 0<=search_index <len(todo_list):
                removedtask=todo_list.pop(search_index)
                print(f"Task Removed{removedtask['Task']}")
            else:
                print("Invalid Task Index")
        except ValueError:
            print("Please Type Valid Choice from above menu")

def task_completed():

    if len(todo_list)==0:
        print("List is empty")
    else:
        try:

            compindex=int(input("Enter the task u completed"))-1;
            if 0<=compindex<len(todo_list):
                todo_list[compindex]['Status']='Done!!'
                print(f"Task {todo_list[compindex]['Task']} has marked as done \n")
            else:
                print("Invalid Task Invalid")
        except ValueError:
            print("Please Type valid choice from above menu")

        


        #function that will display the menu
def menu():
    while(True):
        print("***Main Menu***")
        print("1.Add a new task")
        print("2.View all tasks")
        print("3.Remove a Task")
        print("4.Mark a task as completed")
        print("5.Exit list")

        choice=input("Enter your choice")   

        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            task_completed()
        elif choice=="5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid Choice! Try again!!!")
        
menu()

        


