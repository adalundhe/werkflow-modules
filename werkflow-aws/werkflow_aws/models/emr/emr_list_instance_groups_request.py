from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListInstanceGroupsRequest(BaseModel):
    ClusterId: StrictStr
    Marker: StrictStr | None = None
