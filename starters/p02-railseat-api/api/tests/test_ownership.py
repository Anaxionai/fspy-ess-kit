"""Passengers see only their own bookings (task 22).

Asha books a seat. Ravi, signed in with his own token, must get 404 on her
PNR for GET and DELETE, her booking must stay unchanged, and Ravi's own list
must be empty. Use @example.com addresses: EmailStr rejects `.test`.
"""

import pytest
from httpx import AsyncClient


@pytest.mark.skip(reason="TODO(task 22)")
@pytest.mark.anyio
async def test_another_passenger_gets_404(
    client: AsyncClient, one_seat: dict[str, int]
) -> None:
    """TODO(task 22):
    - sign up and log in Asha and Ravi through /auth/signup and /auth/login,
      and keep each access_token;
    - Asha books the seat in `one_seat`, with `headers={"Authorization": f"Bearer {token}"}`;
    - with Ravi's token, GET and DELETE /bookings/<Asha's PNR> both answer 404;
    - with Asha's token, GET /bookings/<PNR> still shows status "confirmed";
    - with Ravi's token, GET /bookings answers 200 with an empty list.
    Delete the @pytest.mark.skip line above when you start.
    """
    raise NotImplementedError(
        "TODO(task 22): prove that Ravi cannot see Asha's booking"
    )
