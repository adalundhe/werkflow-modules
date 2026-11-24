from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AccessAnalyzerGetGeneratedPolicyRequest(BaseModel):
    jobId: StrictStr
    includeResourcePlaceholders: StrictBool | None = None
    includeServiceLevelTemplate: StrictBool | None = None
