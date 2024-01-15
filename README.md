# DevSearch

## Installation
#### 1. Clone the project:
```
git clone https://github.com/toshko2312/Devs-platform.git
```
#### 2. Create .env file (or rename and modify .env.example) in project root and set environment variables for application

#### 3. Install the modules listed in the `requirements.txt` file (make sure that you are in the `src/` directory):
```
pip install -r requirements.txt
```
#### 4. Start the application (make sure that you are in the `src/` directory):
```
python manage.py runserver
```

## Features
- Features, related to Developers:
  * Create/Edit/Delite profile
  * Email notifications/password reset
  * Create/Edit/Delete skills
  * Read/Send messages to other users
 
- Features, related to Projects:
  * Create/Edit/Delete projects
  * Create/Delete tags
 
 ## Preview
![image](https://github.com/toshko2312/Devs-platform/assets/138567305/b73e2222-24b3-4936-9d80-d45830d12825)
![image](https://github.com/toshko2312/Devs-platform/assets/138567305/c3f2faa5-8656-4a37-baad-566be7947d23)
![image](https://github.com/toshko2312/Devs-platform/assets/138567305/87c55230-4bea-44ae-a751-82c13a056631)
![image](https://github.com/toshko2312/Devs-platform/assets/138567305/1afa13f6-20cb-43b3-b84a-a299c69d71e2)
![image](https://github.com/toshko2312/Devs-platform/assets/138567305/8a4cdd84-458c-4751-85d0-83c45d71bfa4)

## Project structure
```
├───src               - source folder.
│   ├───api           - project api.
│   ├───app           - main app.
│   ├───projects      - projects app.
│   ├───static        - static files.
│   ├───templates     - html templates.
│   ├───users         - users app.
```
## License
This project is licensed under the terms of MIT license.
