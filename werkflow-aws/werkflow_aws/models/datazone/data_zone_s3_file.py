from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneS3File(BaseModel):
    key: StrictStr | None = None
