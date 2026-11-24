from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointContactCenterActivity(BaseModel):
    NextActivity: StrictStr | None = None
