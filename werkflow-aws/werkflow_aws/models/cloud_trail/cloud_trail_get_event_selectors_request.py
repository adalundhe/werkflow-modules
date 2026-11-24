from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetEventSelectorsRequest(BaseModel):
    TrailName: StrictStr
