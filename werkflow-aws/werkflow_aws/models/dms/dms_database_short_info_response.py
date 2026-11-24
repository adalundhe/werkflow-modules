from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDatabaseShortInfoResponse(BaseModel):
    DatabaseId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DatabaseIpAddress: StrictStr | None = None
    DatabaseEngine: StrictStr | None = None
