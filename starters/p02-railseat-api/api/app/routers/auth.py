"""Sign-up and log-in: POST /auth/signup and POST /auth/login (task 22).

The helpers live in app/security.py. Include this router in app/main.py.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

# TODO(task 22): in app/schemas.py, add the request and response models:
#   - SignupIn: email (EmailStr, which needs email-validator) and password
#     (str, at least 10 characters, with Field(min_length=10));
#   - UserOut: id and email;
#   - TokenOut: access_token and token_type ("bearer").
#   LoginIn can use the same two fields as SignupIn.
#
# TODO(task 22): POST /auth/signup, answering 201 with UserOut.
#   Lower-case the email. A taken email gets 409. Store hash_password(...),
#   never the password.
#
# TODO(task 22): POST /auth/login, answering TokenOut.
#   A wrong email and a wrong password get the same 401, so log-in never tells
#   anyone which emails have accounts. Otherwise make a token with
#   secrets.token_urlsafe(32), save hash_token(token) in AuthToken with an
#   expiry 24 hours from now, and return {"access_token": token, "token_type": "bearer"}.
#
# Each route gets the session with `session: AsyncSession = Depends(get_session)`.
