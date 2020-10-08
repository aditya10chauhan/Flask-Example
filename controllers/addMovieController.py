from datetime import datetime
from flask import render_template, request, current_app, redirect, url_for
from models.movie import Movie

def movie_add_page():
    if request.method == "GET":
        values = {"title": "", "year": ""}
        return render_template(
            "movie_edit.html",
            min_year=1887, 
            max_year=datetime.now().year,
            values=values
        )
    else:
        form_title = request.form["title"]
        form_year = request.form["year"]
        movie = Movie(form_title, year=int(form_year) if form_year else None)
        db = current_app.config["db"]
        db.add_movie(movie)
        return redirect(url_for("movies_page"))