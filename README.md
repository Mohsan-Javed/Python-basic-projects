# My Python Learning Journey 🚀

This repository tracks my progress as I learn Python through project-based learning. Each project explores new concepts and builds upon the last.

## Projects

### 1. CLI Task Manager ✅
**Description**: A terminal-based To-Do list application that allows users to add, view, and delete tasks. It includes data persistence, meaning tasks are saved to a file and remembered even after the program closes.

**What I Learnt**:
- **Lists & Methods**: Using `.append()` to add items and `.pop()` to remove them.
- **Loops**: Using `while True` to keep the application running until the user chooses to exit.
- **Conditionals**: Using `if/elif/else` for menu navigation and error checking.
- **Built-in Functions**: `enumerate()` for numbered lists, `len()` for size, and `int()` for type conversion.
- **File I/O**: The `with open()` pattern for reading and writing to `tasks.txt`.
- **Error Handling**: Using `try...except` to prevent the program from crashing on invalid inputs.

**Why it was Beneficial**:
This project laid the foundation for how software handles data and user interaction. It taught me how to move from "in-memory" data (which disappears) to "persistent" data (which stays), a core concept in almost every real-world application.

### 2. Contact Book ✅
**Description**: A more advanced CLI application to manage a list of contacts. Each contact stores multiple pieces of information (Name, Phone, Email). It uses JSON for professional data storage.

**What I Learnt**:
- **Dictionaries**: Storing structured data as Key-Value pairs.
- **JSON Module**: Using `json.dump()` and `json.load()` to save/load complex data (lists of dictionaries).
- **Advanced Search**: Implementing case-insensitive searching using `.lower()` and `.strip()`.
- **Logic Flags**: Using boolean variables (`found = True/False`) to track search results inside loops.
- **Improved Deletion**: Learning how to iterate through a list of dictionaries to find and remove a specific entry by its attributes.

**Why it was Beneficial**:
This project introduced "structured data," which is how real apps handle complex information. Learning JSON is particularly important because it's the standard format for how the internet communicates data between systems.

---
*More projects coming soon...*
