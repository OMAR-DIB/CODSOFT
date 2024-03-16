tasks = []

def listTask():
    count=0
    for i in tasks:
        count+=1
        print(f"{count}. {i}")
        


def addTask():
    task=input("Enter a task: ")
    tasks.append(task)
    print(f"{task}, was added to the list")

def deleteTask():
    listTask()
    try:
        taskDelete=int(input("enter the nb of task: "))
        tasks.pop(taskDelete-1) 
        print(f"task {taskDelete}.was deleted")
    except:
        invalid()

def goodBye():
    print("Good Byeeeeee")

def invalid():
    print("invalid input") 
        
if __name__=="__main__":
    
    print("welcome to the to do list:")
    while True:
        print("\n")
        print("please select one of the next option")
        print("1. list the option ")
        print("2. add option ")
        print("3. Delete option")
        print("4. Quit")

        chose =input("ENTER A NB: ")

        if chose=='1':
            listTask()
        elif chose=='2':
            addTask()
        elif chose=='3':
            deleteTask()
        elif chose=='4':
            goodBye()
            break
        else:
            invalid()