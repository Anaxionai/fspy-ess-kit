"""Sign-in helpers: password hashing, session tokens and the current user (task 22).

Before task 22, add the two packages it needs. In railseat/api/:

    uv add "pwdlib[argon2]" email-validator

Then import `PasswordHash` from `pwdlib` here. Never log or store a plain password.
"""

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session

# auto_error=False: a request with no token reaches current_user with None,
# so your code decides the answer (401), not FastAPI's default.
bearer = HTTPBearer(auto_error=False)


def hash_password(password: str) -> str:
    """Return the argon2 hash of `password`, made with `PasswordHash.recommended()`."""
    raise NotImplementedError("TODO(task 22): hash the password with pwdlib")


def verify_password(password: str, password_hash: str) -> bool:
    """Return True when `password` matches the stored `password_hash`."""
    raise NotImplementedError("TODO(task 22): check the password against its hash")


def hash_token(token: str) -> str:
    """Return the SHA-256 hex digest of a session token.

    The database keeps only this hash. Log-in gives the token itself to the
    user once, and current_user hashes the token it receives to find the row.
    """
    raise NotImplementedError("TODO(task 22): hash the token with hashlib.sha256")


async def current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
    session: AsyncSession = Depends(get_session),
):
    """Return the User whose token came in the `Authorization: Bearer <token>` header.

    TODO(task 22):
    - no credentials: raise HTTPException(401);
    - hash `credentials.credentials` with hash_token, and find an AuthToken with
      that token_hash whose expires_at is still in the future, else 401;
    - return its User (annotate the return type once the User model exists);
    - end with `await session.commit()`, so book_seat can open its own
      transaction in the same request.
    """
    raise NotImplementedError(
        "TODO(task 22): find the user of this token, or answer 401"
    )
