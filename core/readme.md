Instructions
1. Download
2. Open with visual studio code

commands
py -m venv venv(optional)
venv\Scripts\activate
pip install -r requirements.txt
cd core
py manage.py runserver

For Stripe payment
1. login to stripe development
2. generate public and secret key

PUBLISHABLE_KEY = '' SECRET_KEY '' STRIPE_ENDPOINT_SECRET = ''

ADMIN LOGIN
http://127.0.0.1:8000/admin
username and password = admin
