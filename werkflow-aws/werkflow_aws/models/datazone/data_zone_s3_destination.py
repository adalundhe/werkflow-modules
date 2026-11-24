from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneS3Destination(BaseModel):
    uri: StrictStr | None = None
