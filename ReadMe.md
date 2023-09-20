Django E-Learning Project Backend
This is the backend implementation of a Django E-Learning web application. The project is built with Django REST framework and PostgreSQL database.

Installation

1.To use the project, first clone the repository:
git clone (https://github.com/Junaid-Wantza/e-learning-backend-django)

2.Then navigate into the project directory:
cd your_repository/backend

3.Create a virtual environment and activate it:
python -m venv env
source env/bin/activate

4.Install the project dependencies:
pip install -r requirements.txt

5.Create a .env file in the project directory and set the following environment variables:
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Replace your_secret_key with your own.

6.Run the project migrations:
python manage.py migrate

7.Create a superuser account:
python manage.py createsuperuser

8.Start the development server:
python manage.py runserver


API Endpoints
The following API endpoints are available:

/api/users/ - list and create courses
/api/users/<int:pk>/ - retrieve, update, and delete courses
/api/profiles/ - list and create user profiles
/api/profiles/<int:pk>/ - retrieve, update, and delete user profiles
/api/courses/ - list and create courses
/api/courses/<int:pk>/ - retrieve, update, and delete courses




Authentication
The project uses session authentication. To authenticate, send a POST request to /api-auth/login/ with the following data:

{
    "username": "your_username",
    "password": "your_password"
}
You can then use the session cookie to authenticate subsequent requests.

