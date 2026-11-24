from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointEndpointUser(BaseModel):
    UserAttributes: dict[StrictStr, list[StrictStr]] | None = None
    UserId: StrictStr | None = None
