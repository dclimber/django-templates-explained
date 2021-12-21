# Base example django project

Basic django project for use in blog articles about django with:

- `python-decouple` to read environment variables;
- `STATICFILES_DIRS` set to `assets` folder;
- `STATIC_ROOT` and `MEDIA_ROOT` set;
- url-paths to serve static and media files in development mode.

## Usage

### With `poetry`:

Create virtual environment and install dependencies:

    poetry install

Activate virtual environment:

    poetry shell  

### With `venv` and `pip`:

Create virtual environment:

    python3 -m venv env

Activate virtual environment:

    source env/bin/activate

Install dependencies:

    pip install -U pip
    pip install -r requirements.txt

---

## LICENSE

MIT
