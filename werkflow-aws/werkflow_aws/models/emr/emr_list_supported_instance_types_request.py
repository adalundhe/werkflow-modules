from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListSupportedInstanceTypesRequest(BaseModel):
    ReleaseLabel: StrictStr
    Marker: StrictStr | None = None
