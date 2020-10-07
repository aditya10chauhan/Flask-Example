from flask import Flask
from alala import home, movies, movie
from database import Database
from movie import Movie

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=home.home_page)
    app.add_url_rule("/movies", view_func=movies.movies_page)
    app.add_url_rule("/movies/<int:movie_key>", view_func=movie.detail_page)

    createMockUpDB(app=app)

    return app

def createMockUpDB(app):
    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five", year=1972))
    db.add_movie(Movie("The Shining"))
    db.add_movie(Movie("絕命終結站2", year=2020))
    app.config["db"] = db

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
