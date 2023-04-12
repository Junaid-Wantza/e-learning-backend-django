SkillingForSuccess E-Learning Project

This is the backend built with Django that enables users to access various courses on different topics and learn at their own pace. It provides a platform for instructors to create and publish their courses online and for students to sign up for these courses, track their progress, and complete assignments.

Features

User registration and authentication
User roles and permissions
Course creation and publishing
Course enrollment and progress tracking
Course assignments and grading
Course discussion forums
Course completion certificates


Installation
To install and run this project on your local machine, follow these steps:

1.Clone the repository:

git clone https://github.com/yourusername/e-learning.git

2.Create a virtual environment and activate it:

python3 -m venv myenv
source myenv/bin/activate

3.Install the dependencies:

pip install -r requirements.txt

4.Set up the database:

python manage.py migrate

5.Create a superuser:

python manage.py createsuperuser

6.Run the server:

python manage.py runserver

7.Access the application at http://localhost:8000/



Usage
Register a new user and log in to access the application.
As an instructor, create a new course and publish it.
As a student, enroll in a course and start learning.
Complete course assignments and track your progress.
Participate in course discussion forums and interact with other students.
Receive a completion certificate upon finishing a course.
Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b my-new-branch.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin my-new-branch.
Submit a pull request.


Credits
This project was created by Junaid and is licensed under the MIT License.