from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRGetAuthorizationTokenRequest(BaseModel):
    registryIds: list[StrictStr] | None = None
