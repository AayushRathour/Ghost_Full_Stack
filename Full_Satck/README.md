# Ghost Full Stack Project

This is a Django-based web application that appears to handle various demo features including deepfake detection, fraud detection, OTP verification, and voice-related functionalities.

## Prerequisites

- Python 3.12+
- Django
- SQLite3 (included with Django)

## Project Structure

```
├── core/               # Core application directory
├── ghost/             # Main project directory
├── static/            # Static files (images)
├── template/          # HTML templates
├── manage.py          # Django management script
└── db.sqlite3         # SQLite database
```

## Setup Instructions

1. Clone the repository:
```bash
git clone "https://github.com/AayushRathour/Ghost_Full_Stack.git"
cd Ghost_Full_stack
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
```

3. Install required dependencies:
```bash
pip install django
# Add any additional requirements your project needs
```

4. Initialize the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to:
- Main page: `http://localhost:8000`
- Admin interface: `http://localhost:8000/admin`

## Available Features

- Deepfake Detection Demo
- Fraud Detection Demo
- OTP Verification Demo
- Voice-related Features

## Project Pages

- `/` - Home page
- `/login` - Login page
- `/deepfake-demo` - Deepfake detection demo
- `/fraud-demo` - Fraud detection demo
- `/otp-demo` - OTP verification demo
- `/voice-demo` - Voice-related demo

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request.


## Contact

Mobile no. : 8770685206