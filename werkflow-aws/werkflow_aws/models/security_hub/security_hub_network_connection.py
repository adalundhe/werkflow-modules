from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubNetworkConnection(BaseModel):
    Direction: StrictStr | None = None
