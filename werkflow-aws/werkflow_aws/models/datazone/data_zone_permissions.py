from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZonePermissions(BaseModel):
    s3: list[StrictStr] | None = None
