# ArticleHub
"A Django-based web application for creating, managing, and browsing articles with a clean UI and interactive features."

📌 Features
✅ User-friendly interface for article management
✅ Responsive design with a modern look
✅ Search functionality to find articles easily
✅ Navigation bar with interactive buttons

🛠️ Installation
1)Clone the repository:
git clone https://github.com/your-username/ArticleHub.git
cd blog

2)Create a virtual environment:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

3)Install dependencies:
pip install -r requirements.txt

4)Run database migrations:
python manage.py migrate

5)Start the development server:
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.


🏗️ Project Structure
ArticleHub/
│── article/             # Main Django app for articles
│── static/css/          # Stylesheets
│── templates/           # HTML templates
│── ArticleHub/          # Django project settings
│── db.sqlite3           # Database file
│── manage.py            # Django management script
│── requirements.txt     # Python dependencies


🚀 Usage
-Navigate through the homepage, about, and contact pages.
-Search for articles using the search bar.
-Click on an article to read it.
