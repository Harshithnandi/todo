import streamlit as st
from utils.data_handler import load_tasks, save_tasks, add_task, delete_task, update_task

# Load tasks from the JSON file
tasks = load_tasks()

# Streamlit page configuration
st.set_page_config(page_title="To-Do List", layout="centered")

st.title("📝 To-Do List App")

# Add a new task
st.header("Add Task")
task_name = st.text_input("Task Name", value="")
if st.button("Add Task"):
    if task_name.strip():
        add_task(task_name)
        st.success(f"Task '{task_name}' added!")
        st.experimental_rerun()
    else:
        st.error("Task name cannot be empty.")

# Display tasks
st.header("Your Tasks")
if tasks:
    for task in tasks:
        col1, col2, col3 = st.columns([6, 3, 1])
        col1.write(f"- {task['name']}")
        if col2.button("Mark as Done", key=f"done-{task['id']}"):
            delete_task(task['id'])
            st.success(f"Task '{task['name']}' marked as done!")
            st.experimental_rerun()
        if col3.button("Edit", key=f"edit-{task['id']}"):
            new_name = st.text_input("Edit Task Name", value=task['name'], key=f"edit-name-{task['id']}")
            if st.button("Save", key=f"save-{task['id']}"):
                update_task(task['id'], new_name)
                st.success(f"Task updated to '{new_name}'!")
                st.experimental_rerun()
else:
    st.info("No tasks available. Add one above!")

st.caption("Built with ❤️ using Streamlit")
