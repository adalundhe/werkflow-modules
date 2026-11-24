from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubNetworkAutonomousSystem(BaseModel):
    Name: StrictStr | None = None
    Number: StrictInt | None = None
