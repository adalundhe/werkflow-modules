from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2DeleteNetworkInsightsAccessScopeAnalysisResponse(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
