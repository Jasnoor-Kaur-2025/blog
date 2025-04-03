# Django Blogging Site

Welcome to your **Django Blogging Site**! 📝🚀 This project allows users to create, edit, and delete blog posts through a custom admin panel with authentication.

## 📌 Features
- User authentication (Admin login required to manage posts)
- Add, edit, and delete blog posts
- Fun, dark, and neon-themed UI
- Secure user management with Django's built-in authentication

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Jasnoor-Kaur-2025/blog.git
cd blog
cd blogProject
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
Enter your username, email, and password when prompted.

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Now open your browser and visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## 🔧 Customizing the Theme
- The dark & neon theme styles are in the HTML code themselves. Modify as you please!

## 📜 Notes
- The **database (`db.sqlite3`) is not included** in GitHub for security reasons.
- Always keep your **`.env` file** secret (if used).

## 🛠️ Future Improvements
- User comments & likes
- Markdown support for blog posts
- Deployment to a hosting service

Happy coding! 🎉
