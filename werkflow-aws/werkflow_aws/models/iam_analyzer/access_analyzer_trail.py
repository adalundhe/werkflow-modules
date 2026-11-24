from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AccessAnalyzerTrail(BaseModel):
    cloudTrailArn: StrictStr
    regions: list[StrictStr] | None = None
    allRegions: StrictBool | None = None
