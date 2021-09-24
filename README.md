# Hello, Alexandry

Alexandry est une simple API programée en Python avec Flask et Flask-RESTX.

## Installation

Vous pouvez utilisez [pip](https://pip.pypa.io/en/stable/) pour installer les dépendances.

```bash
pip install -r REQUIREMENTS
```

Ensuite, vous devez configurer FLASK_APP et FLASK_ENV.
```bash
export FLASK_APP=hello
export FLASK_ENV=development
```
```cmd
$env:FLASK_ENV = "development" 
$env:FLASK_APP = "main.py"
```

Dans le dossier src, vous pouvez lancer l'application avec la commande :
```bash
flask run
```

C'est tout ! Le serveur est disponible [ici](http://127.0.0.1:5000/)

## License
[MIT](https://choosealicense.com/licenses/mit/)