import os
from flask import Flask, render_template, request, current_app
from flask_pager import Pager
app = Flask(__name__)
app.secret_key = os.urandom(42)
app.config['PAGE_SIZE'] = 20
app.config['VISIBLE_PAGE_COUNT'] = 10


@app.route("/")
def index():
    page = int(request.args.get('page', 1))
    count = 300
    data = range(count)
    pager = Pager(page, count)
    pages = pager.get_pages()
    skip = (page - 1) * current_app.config['PAGE_SIZE']
    limit = current_app.config['PAGE_SIZE']
    data_to_show = data[skip: skip + limit]
    return render_template('index.html', pages=pages, data_to_show=data_to_show)


if __name__ == '__main__':
    app.run(debug=True)
