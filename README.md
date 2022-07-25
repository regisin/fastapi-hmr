# FastAPI Hot Module Reload

This is not a package, just a companion repo to the tutorial found on (my blog)[https://www.paregis.me/posts/fastapi-frontend-development].

It's a proof-of-concept of how you can use FastAPI to develop the frontend of a website with hot reload in development mode.

# Usage

To test things out, I assume you already have `python` installed. This project used 3.10, but earlier versions should work too.

```bash
git clone https://github.com/regisin/fastapi-hmr.git
cd fastapi-hmr
python -m venv env
source env/bin/activate
uvicorn main:app --reload --reload-include '*.html'
```

With the server running, point the browser to `http://localhost:8000`, Then try to edit the source files to change the HTML output (e.g. `/templates/Home.html`). The changes should reflect on the browser without the need for manual refresh.
