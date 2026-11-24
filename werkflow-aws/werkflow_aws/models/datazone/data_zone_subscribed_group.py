from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedGroup(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
