# Masterblog API

Flask blog project with a REST API backend and a separate frontend app.

## Functions

`backend/backend_app.py` (API)

- `get_posts()`: Returns all posts, with optional sorting via query params.
- `add_post()`: Adds a new post from JSON body (`title`, `content`).
- `delete_post(id)`: Deletes a post by id.
- `update_post(id)`: Updates post title/content by id.
- `search_post()`: Filters posts by `title` and/or `content` query params.

`frontend/frontend_app.py`

- `home()`: Renders the frontend page (`index.html`).

## Run

```bash
# Terminal 1: backend API
cd Assessment/Masterblog-API/backend
python backend_app.py

# Terminal 2: frontend
cd Assessment/Masterblog-API/frontend
python frontend_app.py
```
