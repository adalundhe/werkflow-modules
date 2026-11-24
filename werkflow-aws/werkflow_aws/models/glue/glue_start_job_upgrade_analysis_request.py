from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueStartJobUpgradeAnalysisRequest(BaseModel):
    jobName: StrictStr
    analysisId: StrictStr | None = None
    upgradeConsent: Literal['APPROVE', 'DECLINE'] | None = None
