from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetSessionRequest(BaseModel):
    Id: StrictStr
    RequestOrigin: StrictStr | None = None
