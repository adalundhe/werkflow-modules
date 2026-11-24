from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayDeleteSamplingRuleRequest(BaseModel):
    RuleName: StrictStr | None = None
    RuleARN: StrictStr | None = None
