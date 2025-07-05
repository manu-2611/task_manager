# 📝 Task Manager API

A simple Django RESTful API for managing tasks with JWT authentication, Swagger documentation, and test coverage.

This project is built using Python 3.12+, Django 5.2, Django REST Framework, SimpleJWT for secure authentication, and drf-yasg for automatically generated API documentation.

## 📋 Tech Stack

- Python 3.12.2
- Django 5.2.4
- Django REST Framework
- SimpleJWT for authentication
- drf-yasg for API docs (Swagger & ReDoc)

## ⚙️ Installation

### Prerequisites

Install Python 3.12 or higher from [python.org](https://www.python.org/downloads/).
Ensure `pip` is installed by running:

```bash
pip --version
```

### Steps

1. **Clone the repository:**

```bash
https://github.com/manu-2611/task_manager.git
cd task_manager
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/scripts/activate
# for windows
venv\Scripts\activate
```

3. **Install the required packages:**

```bash
pip install -r req.txt
```

4. Run migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Set up environment variables: (If required, to add all db details)**

```bash
REDIS_HOST="REDIS_HOST"
REDIS_PORT="REDIS_PORT"
REDIS_DB="REDIS_DB"
STATIC_TOKEN="STATIC_TOKEN"
JSON_FILE_PATH="JSON_FILE_PATH"
SQL_HOST="SQL_HOST"
SQL_PORT="SQL_PORT"
DB_NAME="DB_NAME"
USERNAME="USERNAME"
PASSWORD="PASSWORD"
```

## Usage

To run the scraping application, follow these steps:

1. **Activate the Virtual Environment**: If you have created a virtual environment, make sure it is activated. In Command Prompt, run:

   ```bash
   venv\Scripts\activate
   ```

2. **Run the Django application**: Start the Django server. Run the following command in your project directory:

   ```bash
   python manage.py runserver
   ```

   3. **Access the API**: Open your web browser and navigate to:

      ```
      http://127.0.0.1:8000/swagger
      http://127.0.0.1:8000/redoc
      ```

      This will open the interactive API documentation where you can test the available endpoints.

## Contributing

We welcome contributions! To get started:

1. **Fork the Repo** and clone it to your machine.
2. **Create a Branch**: `git checkout -b feature/your-feature-name`.
3. **Make Changes** and commit: `git commit -m "Your message"` pre commit will fix the code structure and then commit again.
4. **Push** your branch: `git push origin feature/your-feature-name`.
5. **Open a Pull Request**.

For issues or feature requests, please open an issue. Thank you for contributing!
