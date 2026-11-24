from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AccessAnalyzerTrailProperties(BaseModel):
    cloudTrailArn: StrictStr | None = None
    regions: list[StrictStr] | None = None
    allRegions: StrictBool | None = None
