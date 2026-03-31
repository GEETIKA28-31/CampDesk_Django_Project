# CampDesk_Django_Project
This is a Django-based web application where students can discover and connect with other students.  Users can:  Browse student profiles ,Save students (like a cart system), Send connection requests, View sent and received requests, Accept or reject requests

📘CampDesk (Django)

🎯 Features

🔐 User Authentication (Login/Register),

👤 Student Profile Management,

⭐ Save Students (Wishlist-like feature),

📩 Send Connection Requests,

📥 View Incoming Requests,

📤 View Sent Requests,

📤 Count number of requests

✅ Accept / ❌ Reject Requests,

🍪 Cookie Consent (Accept/Reject),

📧 Email Notifications (for actions like requests)

🛠️ Tech Stack

Backend: Django (Python);
Frontend: HTML, CSS, Bootstrap;
Database: SQLite (default);
Email Service: Gmail SMTP (using App Password);

⚠️ Do not expose your email credentials. Store them in environment variables (.env file).

project/

│── app/  

│   ├── migrations/  

│   ├── models.py  

│   ├── views.py 

│   ├── forms.py   

│   ├── urls.py  

│   ├── admin.py  

│
│── project/     

│   ├── settings.py 

│   ├── urls.py   

│   ├── asgi.py

│   ├── wsgi.py

│
│── templates/               
│
│── static/                  
│
│── media/                   
│
│── db.sqlite3              
|
│── .gitignore 

│── requirements.txt  

│── README.md

│── LICENSE

│── manage.py

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/student-connection-system.git

cd student-connection-system

Create virtual environment

python -m venv env

env\Scripts\activate   # Windows

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Start server

python manage.py runserver

🧪 Usage

Register a new account

Login to dashboard

Browse students

Save students you like

Send connection requests

Manage incoming and sent requests

🔄 CRUD Functionality

The application fully supports CRUD (Create, Read, Update, Delete) operations for student data.

Create: Add new students using forms

Read: Browse and view student profiles

Update: Edit student details

Delete: Remove students from the system

CRUD operations are enhanced with inline form actions, allowing users to perform actions like adding or saving students directly from the browse page without navigation.

👉 These operations are integrated with Django Models and Forms for efficient data handling.

📸 Screenshots (Optional)

Add screenshots of your UI here (Home, Dashboard, Requests, etc.)

🔮 Future Enhancements

💬 Real-time chat system

🔔 Notifications system

🔍 Advanced search & filters

📱 Mobile responsiveness improvements

🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

📄 License

This project is for educational purposes.

👨‍💻 Author

GEETIKA28-31
