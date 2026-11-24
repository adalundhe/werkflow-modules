from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAdditionalAttributes(BaseModel):
    formNames: list[StrictStr] | None = None
