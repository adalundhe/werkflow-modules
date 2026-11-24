from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailTrailInfo(BaseModel):
    TrailARN: StrictStr | None = None
    Name: StrictStr | None = None
    HomeRegion: StrictStr | None = None
