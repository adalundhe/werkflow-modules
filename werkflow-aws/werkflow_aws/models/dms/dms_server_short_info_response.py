from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSServerShortInfoResponse(BaseModel):
    ServerId: StrictStr | None = None
    IpAddress: StrictStr | None = None
    ServerName: StrictStr | None = None
