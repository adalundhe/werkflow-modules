from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedGroupInput(BaseModel):
    identifier: StrictStr | None = None
