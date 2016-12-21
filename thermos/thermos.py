from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfe\xd0>\xf2\x9ds\x1b\xa6N#;\xfd\xec#\x8a\xa7\xd3g\x93\t~\xe8l\xb1'

bookmarks = []


def store_bookmark(url, description):
    bookmarks.append(dict(url=url,
                          description=description,
                          user= "Stasiu",
                          date= datetime.utcnow()))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Moj tytul z kodu",
                           text="To dziala calkiem fajnie jak na razie.",
                           new_bookmarks=new_bookmarks(5)
                           )

@app.route("/add", methods=['GET','POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        app.logger.debug('stored url ' + url)
        flash("Stored '{0}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')