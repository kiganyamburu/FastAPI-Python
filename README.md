# FastAPI Task Manager

This is a simple Task Manager API built with [FastAPI](https://fastapi.tiangolo.com/). It allows you to create, read, update, and delete tasks using RESTful endpoints.

## Features
- Create a new task
- List all tasks
- Retrieve a task by ID
- Update a task
- Delete a task

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation
1. Clone the repository or download the source code.
2. Install the dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Running the Server
Start the development server using Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be available at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### Create a Task
- **POST** `/tasks/`
- Request body: JSON with `title`, `description` (optional), `completed` (default: true)
- Response: Created task object

### List All Tasks
- **GET** `/tasks/`
- Response: List of all tasks

### Get a Task by ID
- **GET** `/tasks/{task_id}`
- Response: Task object

### Update a Task
- **PUT** `/tasks/{task_id}`
- Request body: JSON with fields to update
- Response: Updated task object

### Delete a Task
- **DELETE** `/tasks/{task_id}`
- Response: Deleted task object

## License
This project is licensed under the MIT License. 