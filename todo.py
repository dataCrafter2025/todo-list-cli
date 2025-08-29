import sqlite3
conn=sqlite3.connect("todo.db")
cursor=conn.cursor()

cursor.execute("""create table if not exists tasks(
               id integer primary key autoincrement,
               task text not null,
               status text default 'pending')""")


conn.commit()




def add_task(task):
    cursor.execute("INSERT INTO tasks(task) values(?)",(task,))
    conn.commit()
    print(" Task Added Succesfully")

def view_tasks():
    cursor.execute("select * from tasks") 
    tasks=cursor.fetchall()

    if not tasks:
        print("not task found ")
    else:
        for row in tasks:
            print(f"{row[0]}.{row[1]}-{row[2]}")

def mark_done(task_id):
    cursor.execute("update  tasks SET status='done' where id=?",(task_id,))
    conn.commit()
    print("Task Mark as Done")

def delete_task(task_id):
    cursor.execute("delete from tasks where id=?",(task_id,))
    conn.commit()
    print("Task deleted successfully")




    


def main():
    while True:
       print("\n----------To Do List Manager ---------")
       print("1. Add Task")
       print("2. View Task")
       print("3. Mark Task as done")
       print("4. Delete Task ")
       print("5. Exit")
       choise=input("Enter Choise")

       if choise =="1":
           task=input("Enter Task")
           add_task(task)
       elif choise =="2":
           view_tasks()
       elif choise =="3":
           task_id=int(input("Enter the task id  to mark as done"))
           mark_done(task_id)
       elif choise =="4":
           task_id=int(input("Enter the task Id To delete"))
           delete_task(task_id)
       elif choise=="5":
           print(".....Exiting Bye See you")
           break
       else: 
           print("Please Enter correct choise")

           3
            





if __name__ == "__main__":
    main()