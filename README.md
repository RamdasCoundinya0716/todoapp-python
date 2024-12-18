## **Documentation**

### 1. **Introduction**
The Command-Line To-Do App is a lightweight Python-based tool that allows users to manage tasks from the command line. It supports adding, listing, deleting, and marking tasks as complete, saving data in a JSON file for persistence.

### 2. **Features**
- Add tasks with descriptions.
- List all tasks with their status (completed or not).
- Delete tasks by their unique ID.
- Mark tasks as completed.

### 3. **Dependencies**
- Python 3.x
- No external dependencies (uses Python's standard library).

---

## **Scope**

### **Target Audience**
- Programmers who prefer command-line tools over graphical interfaces.
- Individuals who need a simple, offline task management solution.

### **Use Cases**
1. Managing a personal to-do list.
2. Keeping track of tasks in a lightweight, distraction-free environment.
3. Quick task management for developers working in the terminal.

---

## **The Problem**

### **Identified Issue**
Many task management applications are bloated with features or require an internet connection. For developers or tech-savvy users, using a GUI-based app for simple task management can be inefficient and distracting.

### **Limitations in Existing Solutions**
- Most apps are feature-heavy and require user accounts.
- No minimalistic, offline options tailored for developers or terminal enthusiasts.
- Lack of privacy in cloud-based task management tools.

---

## **The Solution**

### **Proposed Approach**
Build a **Command-Line To-Do App** that:
1. Operates entirely offline.
2. Provides essential task management features without unnecessary complexity.
3. Saves data locally in a JSON file, ensuring privacy.
4. Allows integration with other terminal-based workflows.

---

## **How Are We Solving It?**

### **Step-by-Step Breakdown**

1. **Command-Line Interface**:
   - Use Python's `argparse` library to create subcommands (`add`, `list`, `delete`, `complete`).
   - Allow users to pass task descriptions and IDs as arguments.

2. **Data Storage**:
   - Store tasks in a JSON file (`tasks.json`), making it easy to read, write, and modify tasks.
   - Each task has:
     - `id`: A unique identifier.
     - `description`: The task's text.
     - `completed`: A boolean indicating whether the task is done.

3. **Core Features**:
   - **Add Task**: Append a new task to the JSON file.
   - **List Tasks**: Display tasks with their status (`✔` or `✗`).
   - **Delete Task**: Remove a task by its unique ID.
   - **Complete Task**: Mark a task as completed and update its status in the JSON file.

4. **User Feedback**:
   - Provide clear output for every command (e.g., "Task added: ...", "Task marked as completed").
   - Handle edge cases (e.g., invalid IDs, empty task lists).

5. **Error Handling**:
   - Check for missing JSON files and create them dynamically.
   - Handle invalid user inputs gracefully (e.g., non-integer task IDs).

---

## **How to Run the Application**

1. Save the code to a file, e.g., `todo.py`.
2. Open a terminal and navigate to the script's directory.
3. Run the following commands to interact with the app:

### Examples:
#### Add a Task:
```bash
python todo.py add "Complete Python project"
```

#### List All Tasks:
```bash
python todo.py list
```

#### Delete a Task:
```bash
python todo.py delete 1
```

#### Complete a Task:
```bash
python todo.py complete 1
```

---

## **Conclusion**

The Command-Line To-Do App is a simple yet powerful solution for managing tasks efficiently in the terminal. By focusing on core features and leveraging Python's standard library, this project demonstrates:
1. Proficiency in Python programming.
2. Familiarity with JSON for data persistence.
3. Practical problem-solving and user-focused design.

This app can be expanded further to include features like due dates, priorities, or integration with other tools, making it a valuable addition to your programming portfolio.
