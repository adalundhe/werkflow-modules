from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserIdentityInfoLite(BaseModel):
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
