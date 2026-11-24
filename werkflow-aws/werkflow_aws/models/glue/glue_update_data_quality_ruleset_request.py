from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateDataQualityRulesetRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Ruleset: StrictStr | None = None
