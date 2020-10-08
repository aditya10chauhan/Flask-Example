from datetime import datetime
from flask import render_template, request, current_app, redirect, url_for, abort
from models.movie import Movie

def movie_edit_page(movie_key):
    if request.method == "GET":
        db = current_app.config["db"]
        movie = db.get_movie(movie_key)
        if movie is None:
            abort(404)
        values = {"title": movie.title, "year": movie.year}
        return render_template(
            "movie_edit.html",
            min_year=1887,
            max_year=datetime.now().year,
            values=values,
        )
    else:
        form_title = request.form["title"]
        form_year = request.form["year"]
        movie = Movie(form_title, year=int(form_year) if form_year else None)
        db = current_app.config["db"]
        db.update_movie(movie_key, movie)
        return redirect(url_for("movies_page"))