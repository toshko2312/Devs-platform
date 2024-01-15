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

## Features:
- Features, related to Developers:
  * Create/Edit/Delite profile
  * Email notifications/password reset
  * Create/Edit/Delete skills
  * Read/Send messages to other users
 
- Features, related to Projects:
  * Create/Edit/Delete projects
  * Create/Delete tags

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
