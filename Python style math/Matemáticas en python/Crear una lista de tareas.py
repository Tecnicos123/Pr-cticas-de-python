list = []

while True:
    task = input("Enter a task (or 'done' to stop): ")
   
    if task == 'done':
        break
    else:
        list.append(task)

print("Your tasks are:")
for task in list:
    print(task)