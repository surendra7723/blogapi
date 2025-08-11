# Blog API

This is a Django-based Blog API project. It provides endpoints for managing blog posts and user accounts.

## Features
- User authentication and registration
- CRUD operations for blog posts
- Permissions and user roles
- Admin interface

## Project Structure
- `accounts/` - User account management (models, views, forms)
- `posts/` - Blog post management (models, views, serializers, permissions)
- `django_project/` - Django project settings and configuration
- `templates/` - HTML templates
- `staicfiles/` - Static files (CSS, JS, images)
- `db.sqlite3` - SQLite database
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd blogapi
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the API endpoints at `http://localhost:8000/`
- Admin interface at `http://localhost:8000/admin/`

## License
This project is licensed under the MIT License.
