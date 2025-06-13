# register-stroke
register-stroke

branch feature/startproject

python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 manage.py runserver
