from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetAppsRequest(BaseModel):
    PageSize: StrictStr | None = None
    Token: StrictStr | None = None
