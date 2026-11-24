from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetServiceLastAccessedDetailsRequest(BaseModel):
    JobId: StrictStr
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
