### Setup du projet

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

.venv\Scripts\Activate

pip freeze > requirements.txt


### Check des guidelines :

ruff check . --fix
black .
mypy .

pre-commit run --all-files
