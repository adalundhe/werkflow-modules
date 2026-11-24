from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneModel(BaseModel):
    smithy: StrictStr | None = None
