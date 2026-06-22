# Day 17 — Reusable Auth & Role Dependencies

Part of a daily FastAPI + SQLAlchemy learning challenge.

## What this builds on
Refactors Day 16's role-based API so that **all authentication and role-checking logic lives in dependency functions**, not inline inside route bodies.

## What's new
- `get_current_user` — decodes the JWT and returns the authenticated user (moved fully into `auth.py`, used via `Depends()`)
- `require_any_role(*roles)` — a reusable dependency factory for role-based access control
- `GET /me` — returns the current logged-in user's profile, regardless of role
- `GET /dashboard` — demonstrates multi-role access (`teacher` and `admin` only)
- Refactored existing routes (`/courses` POST, `/users` GET) to use `Depends()` for role checks instead of inline `if` statements

## Tech stack
FastAPI · SQLAlchemy · SQLite · Pydantic · python-jose · passlib (bcrypt)

## Running locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open `http://127.0.0.1:8000/docs` for Swagger UI.

## Testing
Tested in Swagger UI with three token types — `student`, `teacher`, and `admin` — plus no token at all, confirming correct `200` / `403` / `401` responses across protected routes.
