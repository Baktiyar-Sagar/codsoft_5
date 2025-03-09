import time
import FreeSimpleGUI as fg
import os

FILEPATH = "todo.txt"
def get_todos(filepath=FILEPATH):
    """Read a txt file and return to-do items in the list"""
    with open(filepath, 'r') as file_local:
      todo_list_local = file_local.readlines()
      return todo_list_local

def write_todo(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        todolist_local = file_local.writelines(todo_arg)
        return todolist_local

def print_list(todo_list_local):
    for index_local, todo_local in enumerate(todo_list_local):
        print(f"No {index_local + 1} item: {todo_local.strip("\n").title()}")

if not os.path.exists("todo.txt"):
    with open ("todo.txt",'w') as file:
        pass


fg.theme("Black")
clock = fg.Text('',key='clock')
label = fg.Text("Type a to-do")
text_box = fg.InputText(tooltip="Please input a todo", key= 'todo')
add_button = fg.Button("Add",size=10)
list_box = fg.Listbox(values=get_todos(),key='todo_box',
                      enable_events=True, size=[44,10])
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")
exit_button = fg.Button("Exit",size=10)

window = fg.Window("To do app",
                   layout=[ [clock],
                           [label],[text_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',12))
while True:
    event , value = window.read(timeout=200)

    window['clock'].update(value=time.strftime("%b %d, %Y | %H:%M:%S"))
    match event:
        case fg.WIN_CLOSED:
            break

        case 'Add':
            todo_list = get_todos()
            new_todo = value['todo'] + '\n'
            todo_list.append(new_todo)
            write_todo(todo_list)
            window['todo_box'].update(values=todo_list)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = value['todo_box'][0]
                new_todo = value['todo']+'\n'
                todo_list = get_todos()
                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo
                write_todo(todo_list)
                window['todo_box'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                fg.popup("Please select an to-do before clicking Edit",title='Error',font='10',text_color='Brown',button_justification='centered')
        case 'Complete':
            try:
                todo_to_complete = value['todo_box'][0]
                todo_list = get_todos()
                todo_list.remove(todo_to_complete)
                write_todo(todo_list)
                window['todo_box'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                fg.popup("Please select an to-do before clicking Complete",title='Error',font='10',text_color='Brown',button_justification='centered')
        case 'Exit':
            break

        case 'todo_box':
            window['todo'].update(value=value['todo_box'][0].strip('\n'))


window.close()