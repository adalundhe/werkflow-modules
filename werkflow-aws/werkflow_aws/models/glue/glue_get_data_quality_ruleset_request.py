from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataQualityRulesetRequest(BaseModel):
    Name: StrictStr
