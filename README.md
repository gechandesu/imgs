# imgs

imgs is simple and minimalictic image sharing web app written in Python using Flask. No database. No image compression. No time limits. No additional dependencies.

The application does not save records about image URLs. Immediately after loading the image, you can copy the direct link and use it anywhere.

This software is intended for personal use and is not suitable for creating a public image hosting. Please do not try to use it for this.

## Usage

TODO

## Installation

Install Python virtual environment:

```
python3 -m venv env
```

Then install Flask:

```
source env/bin/activate
pip install flask
```

Clone imgs from repo:

```
git clone https://github.com/gechandesu/imgs
cd imgs
```

Edit the `config.py`. Change path to `UPLOADS_FOLDER` and set `APP_URL`. It's `http://127.0.0.1:5000/` by default.

```
APP_URL = 'http://127.0.0.1:5000/' # "/" in end is important!
UPLOADS_FOLDER = '/mnt/develop/imgs/imgs/uploads/'```
```

Run imgs:

```
python3 main.py
```

Check the http://127.0.0.1:5000/ in browser. You can already upload pictures to the application.

You can also deploy it on the server in a typical Flask manner. As an example with uWSGI+Nginx. Read the Flask docs: [https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/](https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

This code is published under Unlicense. See [LICENSE.md](LICENSE.md).
