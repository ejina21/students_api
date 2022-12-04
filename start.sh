#bin/bash
echo '###create venv'
python3 -m venv venv

echo '###activate venv'
source venv/bin/activate

echo '###install requrements'
pip install -r requirements.txt

echo '###run migrate'
python3 manage.py migrate

echo '###pull db'
python3 pull_db.py

echo '###start app'
python3 manage.py runserver