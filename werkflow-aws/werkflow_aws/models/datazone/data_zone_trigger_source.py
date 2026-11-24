from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneTriggerSource(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
