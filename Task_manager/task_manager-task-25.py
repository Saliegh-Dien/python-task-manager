import datetime
from datetime import date

#this is the section login section--------------------------------------------------------------------------------------

#empty strings
user_names = ""
pass_words = ""

#opens files
file = open("user.txt", "r")
user_file = file.readlines()

#this loop gathers the data of text file and strips(", "),being left with 2 words,the username and password
#and adding them to the empty strings
#nizaam(mentor) showed me this part, my loop was working incorrectly
for line in user_file:
    temp = line.split(", ")
    user_names += temp[0]
    pass_words += temp[1]

#declared false boolean
logged_in = False

#this loop determines whether input is valid according to data on text file and if valid, converts boolean to true
while not logged_in:
    username = input("Username: ")
    password = input("Password: ")
    if username in user_names and password in pass_words:
        logged_in = True
        print("login successful!")
    else:
        print("invalid info")
file.close()
# ======================================================================================================================
#register user function
def reg_user():
    # this block opens files
    text_A = open("tasks.txt", "r+")
    text_B = open("user.txt", "r+")
    file_A = text_A.read()
    file_B = text_B.read()

    # this block stores user's input and writes onto text file
    username = input("Username: ")
    password = input("Password: ")
    while username in file_B:
        print("username already exists\nplease try again: ")
        username = input("Username: ")
        password = input("Password: ")


    while username not in text_B:
        u_p = username + ", " + password
        u_p = u_p.split(",")
        u_p2 = []

        for i in u_p:
            u_p2.append(i)
        text_B.write(f"""\n{username}, {password} """)
        break
    text_B.close()
# this section confirms registration------------------------------------------------------------------------------------
    user_names = ""
    pass_words = ""
    # empty strings

    # opens files
    file = open("user.txt", "r")
    user_file = file.readlines()

    # this loop gathers the data of text file and strips(", "),being left with 2 words,the username and password
    # and adding them to the empty strings
    # nizaam(mentor) helped me with this part, my loop was working incorrectly
    for line in user_file:
        temp = line.split(", ")
        user_names += temp[0]
        pass_words += temp[1]

    # declared false boolean
    logged_in = False

    # this loop determines whether input is valid according to data on text file and if valid, converts boolean to true
    while not logged_in:
        print("Confirm registration:")
        username = input("Username: ")
        password = input("Password: ")

        # if statement allows login if information is valid
        if username in user_names and password in pass_words:
            logged_in = True
            print("registration confirmed")
        else:
            print("registration not confirmed")

    # closes file
    return file.close()

# ======================================================================================================================
#add task function------------------------------------------------------------------------------------------------------
from  datetime import date
#importing date, needed to get today's date

def add_task():
    tasks_file = open("tasks.txt", "a")
    task_doer = str(input("Username of person task is being assigned to: "))
    task_title = str(input("Title of task: "))
    task_descrip = str(input("Description of task: "))
    today = date.today()
    date_assigned = today.strftime("%d %m %Y")
    task_assigned = str(date_assigned)
    # Date function to add today's date and in different format which mentor nizaam explained to me
    task_due_date = str(input("Task due date: "))
    task_done = "No"

    # this block adds inputted information together
    task = task_doer + ", " + task_title + ", " + task_descrip + ", " + str(task_assigned) + ", " + str(
        task_due_date) + ", " + task_done
    task = task.split(",")
    full_task = []

    # this block writes the inputted data as a string in 1 line onto text file
    for i in task:
        full_task.append(i)
    tasks_file.write(f"""\n{",".join(full_task)} """)
    return tasks_file.close()

# ======================================================================================================================
#view all function
def view_all():
    tasks_file = open("tasks.txt", "r")
    tasks_file_read = tasks_file.readlines()

    # this loop prints desired indexed data from text file in appropriate order
    # this method was taught to me by nizaam(mentor)
    for i in tasks_file_read:
        x = i.strip()
        x = x.split(", ")
        print("")
        print(" User:           :{}".format(x[0]))
        print(" Task title:         :{}".format(x[1]))
        print(" Task description:   :{}".format(x[2]))
        print(" Task due date:      :{}".format(x[3]))
        print(" Task assigned:      :{}".format(x[4]))
        print(" Task done:          :{}".format(x[5]))

    # closes file
    return tasks_file.close()

#=======================================================================================================================
#view mine function
def view_mine():
    # this block will open text files, include a counter for numbering user's tasks, empty list
    # Importing modules to edit files (file input and NewType)
    import fileinput
    from typing import NewType
    tasks_text = open("tasks.txt", "r")
    tasks_text = tasks_text.readlines()
    task_num = 0
    users_tasks = []

    # this block numbers and displays user's tasks in easy to read format
    for content in tasks_text:
        task_user, tasks_title, task_description, date_assigned, due_date, task_completion = content.split(", ")
        users_tasks.append(content)
        # appends the data to the empty list

        if username == task_user:
            task_num += 1
            print(f"Task assigned to:    {task_user}")
            print(f"Task number:         {task_num}")
            print(f"Task title:          {tasks_title}")
            print(f"Task description:    {task_description}")
            print(f"Date assigned:       {date_assigned}")
            print(f"Due date:            {due_date}")
            print(f"Task completed:      {task_completion}\n")

    # user input to select specific task to edit
    edit = input("Select task number to be edited: ")

    if edit != "-1":
        index = int(edit) - 1
        # subtracting 1 from the user input to get the correct index to reference in the file (first index = 0)
        line_list = users_tasks[index]
        task_user, tasks_title, task_description, date_assigned, due_date, task_completion = line_list.split(", ")
        # Assigning a variable to each index of the lines of the text file (each line should have 6 indexes)

        if task_completion == task_completion.strip("\n"):
            # When the tasks get written into the file, it will be written without open lines
            new_line = False
        else:
            new_line = True
        task_completion = task_completion.strip("\n")
        edit_task_completion = input("m - Mark task as complete \ne - Edit task \nEnter m/e: ")

        # converts last index of line in text file into "yes", marking it complete
        if edit_task_completion == "m":
            task_completion = "Yes"

        # edits task
        elif edit_task_completion == "e":
            # edits task user
            new_user = input("Enter the username to assign the task to:")
            task_user = new_user
            # edits task's due date
            new_date = input("Enter new due date of task")
            due_date = new_date

        if new_line == True:
            # this will add a new line after last index, otherwise line that was supposed to be next will mix with this line
            task_completion += "\n"

        # this is the new task information(new line to go into text file)
        new_edited_task = f"{task_user}, {tasks_title}, {task_description}, {date_assigned}, {due_date}, {task_completion}"

        old_task = users_tasks[index]
        task_index = 0

        # loop that does the replacing
        for content in users_tasks:
            if old_task == content:
                users_tasks[task_index] = new_edited_task
            task_index += 1

        # writing new edited information of task into text file
        with open("tasks.txt", "w") as new_data:
            new_data.writelines(users_tasks)

#=======================================================================================================================
def statistics():

    #this block opens files only if user is the admin
    if order == "ds" and username == "admin":
        usersAmount = open("user.txt", "r")
        tasksAmount = open("tasks.txt", "r")

        #count to count lines in text file (1 line = 1 task)
        users_count = 0
        tasks_count = 0

        # counts amount of users registered onto text file
        for i in usersAmount:
            users_count += 1
        print("Total users: " + str(users_count))

        # counts amount of tasks registered onto text file
        for i in tasksAmount:
            tasks_count += 1
        print("Total tasks: " + str(tasks_count))


#=======================================================================================================================
def generate_reports():
#TASK OVERVIEW

    #this block opens the text file and splits it, includes a counter
    with open("tasks.txt", "r") as tasks_text:
        tasks_counter = 0
        tasks_text_read = tasks_text.read()
        tasks_split = tasks_text_read.split("\n")

    #this loop counts the lines in the task text file
        for i in tasks_split:
            if i:
                tasks_counter += 1

# Counting the completed and uncompleted tasks in the task file
    with open("tasks.txt", "r") as tasks_text:
        tasks_text_read = tasks_text.read()
        completed_tasks_amount = tasks_text_read.count("Yes")
        incompleted_tasks_amount = tasks_text_read.count("No")

# Opening and reading the tasks text file in order to generate reports
    with open("tasks.txt", "r") as tasks_text:

        today = datetime.datetime.today()
        tasks_text_readlines = tasks_text.readlines()
        incompleted_tasks_overdue = 0

        for i in tasks_text_readlines:
            lines = i.strip().split(", ")

# Stripping the date from the tasks to use in calculations,
#i got the method from https://www.programiz.com/python-programming/datetime/strptime
#this method was taught to me by a fellow classmate from hyperiondev, showed me where to research
            if datetime.datetime.strptime(lines[-2], "%d %m %Y") < today and lines[-1] == "No":
                incompleted_tasks_overdue += 1

# Calculating percentage of tasks that are not complete and rounding it off
    all_incompleted = incompleted_tasks_amount / tasks_counter * 100
    rounded_incompleted = round(all_incompleted, 2)

# Calculating percentage of tasks that are overdue and incomplete, then rounding it off
    overdue_incompleted = incompleted_tasks_overdue / tasks_counter * 100
    rounded_overdue_incompleted = round(overdue_incompleted, 2)

    #this block converts the data of variables into strings so to then write them into text file
    with open("task_overview.txt", "w") as task_overview:
        str_tasks_counter = str(tasks_counter)
        str_completed_tasks_amount = str(completed_tasks_amount)
        str_incompleted_tasks_amount = str(incompleted_tasks_amount)
        str_incompleted_tasks_overdue = str(incompleted_tasks_overdue)
        str_rounded_incompleted = str(rounded_incompleted)
        str_rounded_overdue_incompleted = str(rounded_overdue_incompleted)

        #this block will write it into text file
        task_overview.write("Task overview: \n")
        task_overview.write("Total number of tasks: " + str_tasks_counter + "\n")
        task_overview.write(str_completed_tasks_amount + " tasks are completed\n")
        task_overview.write(str_incompleted_tasks_amount + " tasks are incomplete\n")
        task_overview.write(str_incompleted_tasks_overdue + " tasks are overdue\n")
        task_overview.write(str_rounded_incompleted + "% of tasks are incomplete\n")
        task_overview.write(str_rounded_overdue_incompleted + "% of tasks are overdue\n")

        #this block displays task overview information in user-friendly manner for user
        print("\nTask overview: ")
        print("Total number of tasks: " + str_tasks_counter)
        print(str_completed_tasks_amount + " tasks are completed")
        print(str_incompleted_tasks_amount + " tasks are incomplete")
        print(str_incompleted_tasks_overdue + " tasks are overdue")
        print(str_rounded_incompleted + "% of tasks are incomplete")
        print(str_rounded_overdue_incompleted + "% of tasks are overdue")

#END OF TASK OVERVIEW
#-----------------------------------------------------------------------------------------------------------------------
#USER OVERVIEW
    with open("user.txt", "r") as user_text:

        user_text_readfile = user_text.read().split("\n")
        #counting in all lines in user text file to get number of users
        amount_of_users = 0

        for line in user_text_readfile:
            if line:
                amount_of_users += 1

    user_overview_file = open("user.txt", "r")
    task_overview_file = open("tasks.txt", "r")
    user_overview_file = user_overview_file.readlines()
    task_overview_file = task_overview_file.readlines()
    num_users = len(user_overview_file)
    print("\nNumber of users: " + str(num_users)) #for control
    list = []


#this block assigns username and password to a variable and stores all usernames into the empty list
    for line in user_overview_file:
        user, password = line.split(", ")
        list.append(user)
    #print(list)#control

#this block opens file to write into, assigns variables to indexes and appends user's task data to a list
    with open("user_overview.txt", "w") as user_overview_text_file:
        for i in list:
            print("username: " + i)#shows user's name
            users_tasks = []

            for line in task_overview_file:
                #print(line)#control
                user, task_title, task_description, date_assigned, due_date, completion_status = line.split(", ")

                if user == i:
                    print(i)#control
                    users_tasks.append(i)
                    #appending user's task lines to the empty list

            #print(str(users_tasks))#control
            total = len(users_tasks)
            #print(total)#control
            overdue_tasks = 0
            completed_tasks = 0

            for i in users_tasks:
                line = i.split(", ")

                #this block counts complete and overdue tasks
                if line[-1] == "Yes":
                    completed_tasks += 1
                if line[-1] == "No":
                    line[-2] = datetime.datetime.strptime(due_date,"%d %m %Y")
                    if line[-2] < today:
                        overdue_tasks += 1

                #this block calculates amount of different classed tasks
                incomplete_tasks = total - completed_tasks
                if total != 0:
                    amount_of_users_tasks = round((total / tasks_counter) * 100, 2)
                    amount_of_tasks_completed = round((completed_tasks / total) * 100, 2)
                    amount_of_incomplete_tasks = round((incomplete_tasks / total) * 100, 2)
                    amount_of_users_task_overdue = round((overdue_tasks / total) * 100, 2)

            #this block writes user overview onto text file
            if total != 0:
                user_overview_text_file.write("User overview: \n")
                user_overview_text_file.write("Number of tasks: " + str(total) + "\n")
                user_overview_text_file.write("Total number of tasks: " + str(tasks_counter))
                user_overview_text_file.write(str(amount_of_users_tasks) + "% of tasks are assigned to user\n")
                user_overview_text_file.write(str(amount_of_tasks_completed) + "% of tasks are complete\n")
                user_overview_text_file.write(str(amount_of_incomplete_tasks) + "% of tasks are incomplete\n")
                user_overview_text_file.write(str(amount_of_users_task_overdue) + "% of tasks are overdue\n")

            #this block displays the user overview information in user-friendly manner for user
                print("\nUser overview: ")
                print("Number of tasks: " + str(total))
                print("Total number of tasks: " + str(tasks_counter))
                print(str(amount_of_users_tasks) + "% of tasks are assigned to user")
                print(str(amount_of_tasks_completed) + "% of tasks are complete")
                print(str(amount_of_incomplete_tasks) + "% of tasks are incomplete")
                print(str(amount_of_users_task_overdue) + "% of tasks are overdue\n")

            else:
                print(" No tasks assigned to this user")

#END OF USER OVERVIEW
#=======================================================================================================================
if username != "admin":
    print("OPTIONS-\nr - register user(admin only)\na - add task\nva - view all tasks\nvm - view my tasks\ne - exit")

if username == "admin":
    print("OPTIONS-\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - statistics\ne - exit")
order = input("Enter one option: ")


#this section adds username and password to text file user.txt----------------------------------------------------------
if order == "r" and username != "admin":
    print("registration is for admin use only")

if order == "r" and username == "admin":
    reg_user()

#this section adds a task-----------------------------------------------------------------------------------------------

if order == "a" :
    add_task()

#this section views all tasks-------------------------------------------------------------------------------------------
#opens files
if order == "va" :
    view_all()

#this section views tasks assigned only to user-------------------------------------------------------------------------
#opens file
if order == "vm" :
    view_mine()

#this section displays statistics for admin view only-------------------------------------------------------------------
#opens files
if order == "ds" and username == "admin":
    statistics()

#this section generates reports-----------------------------------------------------------------------------------------
if order == "gr" :
    generate_reports()

# this section is for the exit option-----------------------------------------------------------------------------------
# learnt about exit function at https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
if order == "e":
    print("Goodbye")
    exit()
