from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerApplyArchiveRuleRequest(BaseModel):
    analyzerArn: StrictStr
    ruleName: StrictStr
    clientToken: StrictStr | None = None
