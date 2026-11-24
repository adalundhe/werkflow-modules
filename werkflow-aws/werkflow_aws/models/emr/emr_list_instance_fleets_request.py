from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListInstanceFleetsRequest(BaseModel):
    ClusterId: StrictStr
    Marker: StrictStr | None = None
