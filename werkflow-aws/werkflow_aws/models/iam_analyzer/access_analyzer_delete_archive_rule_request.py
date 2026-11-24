from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerDeleteArchiveRuleRequest(BaseModel):
    analyzerName: StrictStr
    ruleName: StrictStr
    clientToken: StrictStr | None = None
