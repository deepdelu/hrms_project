HRMS Project

To run the project, follow these steps:

1. Install the following applications:
   - Visual Studio Code - Download from: https://code.visualstudio.com/Download
   - Python - Download from: https://www.python.org/downloads/
   - DB Browser (SQLite) - Download from: https://sqlitebrowser.org/dl/

2. After installing the applications, navigate to the project's root directory where you can find the Python file named "manage.py". Open this directory using Visual Studio Code.

3. Open the terminal in Visual Studio Code and execute the following commands:

   - Install Django by running the following command in the terminal:
     pip install django

   - Create the database by running these two commands:
     python manage.py makemigrations
     python manage.py migrate

4. The project setup is now complete.

5. To run the project, use this command in the terminal:
   python manage.py runserver

6. The server will start, and a link (http://127.0.0.1:8000/) will be displayed. Copy this link and paste it into any web browser to access the website.
