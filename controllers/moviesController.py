from flask import render_template, current_app, request, redirect, url_for
import database

def movies_page():
    db = current_app.config["db"]
    if request.method == 'GET':
        movies = db.get_movies()
        # default sort by the first element of pair (title, year)
        return render_template("movies.html", movies=sorted(movies))
    else:
        form_movies_keys = request.form.getlist('movie_keys')
        for select_key in form_movies_keys:
            db.delete_movie(int(select_key))
        return redirect(url_for("movies_page"))
    