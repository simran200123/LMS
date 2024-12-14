# LMS
Prerequisites
Python Installation:

Download and install Python from python.org.
During installation, check "Add Python to PATH".
Install Django:

Open Command Prompt or Terminal and run:
bash
Copy code
pip install django
Extract the Project:

Download and extract the project zip file.
Navigate into the extracted lms_project directory.
Steps to Run the Project
1. Navigate to the Project Folder
Open Command Prompt or Terminal and move to the folder containing manage.py:

bash
Copy code
cd path_to_extracted_folder/lms_project
2. Set Up the Database
Initialize the database and apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
3. Create a Superuser
Create an admin account to manage the app:

bash
Copy code
python manage.py createsuperuser
Enter a username, email address, and password.
4. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
The server will start at http://127.0.0.1:8000/.
In the server address add 'http://127.0.0.1:8000/admin'
