from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetJobUpgradeAnalysisResponse(BaseModel):
    jobName: StrictStr | None = None
    analysisId: StrictStr | None = None
    status: StrictStr | None = None
    sourceVersion: StrictStr | None = None
    targetVersion: StrictStr | None = None
    analysisType: StrictStr | None = None
    autoUpgradeEvaluationSummary: StrictStr | None = None
    errorMessage: StrictStr | None = None
    autoUpgradeEligibilitySummary: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
