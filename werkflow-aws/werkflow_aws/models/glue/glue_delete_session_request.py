from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteSessionRequest(BaseModel):
    Id: StrictStr
    RequestOrigin: StrictStr | None = None
