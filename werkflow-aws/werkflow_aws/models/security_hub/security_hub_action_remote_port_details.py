from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubActionRemotePortDetails(BaseModel):
    Port: StrictInt | None = None
    PortName: StrictStr | None = None
