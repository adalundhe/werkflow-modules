from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserIdentityInfo(BaseModel):
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
    Email: StrictStr | None = None
    SecondaryEmail: StrictStr | None = None
    Mobile: StrictStr | None = None
