from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEndpointInfo(BaseModel):
    Type: StrictStr | None = None
    Address: StrictStr | None = None
    DisplayName: StrictStr | None = None
