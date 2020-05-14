# Python Flask Movie-list Api

> Python Flask backend app for keeping track of todos.  It uses a flask sqlite database along with flask-marshmallow for object serialization/deserialization.  You can Post, Get, Patch(Eventually), and Delete todos through flask routes.

- Dependencies
  - Python
    - [python](https://www.python.org/)
  - Flask
    - [flask-pypi](https://pypi.org/project/Flask/)
    - [flask-docs](https://flask.palletsprojects.com/en/1.1.x/)
  - Flask-SQLAlchemy
    - [flask-sqlalchemy-pypi](https://pypi.org/project/Flask-SQLAlchemy/)
    - [flask-sqlalchemy-docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - Flask-Marshmallow
    - [flask-marshmallow-pypi](https://pypi.org/project/flask-marshmallow/)
    - [flask-marshmallow-docs](https://flask-marshmallow.readthedocs.io/)
  - Flask-Cors
    - [flask-cors-pypi](https://pypi.org/project/Flask-Cors/)
    - [flask-cors-docs](https://flask-cors.readthedocs.io/en/latest/)

- Install all dependencies
```
$ pipenv install Flask Flask-SQLAlchemy flask-marshmallow Flask-Cors
```

- Create your sqlite database
```
$ pipenv shell
$ python
>>> from app import db
>>> db.create_all()
```

- Flask Routes
  - POST One Movie
    - http://localhost:5000/api/v1/movie
    ```json
    {
        "title": "Scary Movie",
        "genre": "Thriller",
        "image_url": "http://cloudinaryimage.com",
        "public_id": "random_public_id"
    }
    ```
  - GET All Movies
    - http://localhost:5000/api/v1/movies
  - DELETE One Movie
    - http://localhost:5000/api/v1/movie/id

