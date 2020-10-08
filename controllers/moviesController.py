from flask import render_template, current_app

def movies_page():
    db = current_app.config["db"]
    movies = db.get_movies()
    # default sort by the first element of pair (title, year)
    return render_template("movies.html", movies=sorted(movies))
    