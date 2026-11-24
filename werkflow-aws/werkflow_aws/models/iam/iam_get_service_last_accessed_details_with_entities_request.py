from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetServiceLastAccessedDetailsWithEntitiesRequest(BaseModel):
    JobId: StrictStr
    ServiceNamespace: StrictStr
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
