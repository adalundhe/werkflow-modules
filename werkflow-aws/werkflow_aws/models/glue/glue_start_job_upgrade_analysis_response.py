from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueStartJobUpgradeAnalysisResponse(BaseModel):
    analysisId: StrictStr | None = None
    jobName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
