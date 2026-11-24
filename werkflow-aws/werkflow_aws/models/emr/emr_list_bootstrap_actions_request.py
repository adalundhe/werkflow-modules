from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRListBootstrapActionsRequest(BaseModel):
    ClusterId: StrictStr
    Marker: StrictStr | None = None
