from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteDataQualityRulesetRequest(BaseModel):
    Name: StrictStr
