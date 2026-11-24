from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetMapStyleDescriptorRequest(BaseModel):
    MapName: StrictStr
    Key: StrictStr | None = None
