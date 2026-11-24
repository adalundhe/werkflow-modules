from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUsernamePassword(BaseModel):
    password: StrictStr | None = None
    username: StrictStr | None = None
