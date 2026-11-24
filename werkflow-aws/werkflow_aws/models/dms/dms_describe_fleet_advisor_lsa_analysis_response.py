from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_fleet_advisor_lsa_analysis_response import DMSFleetAdvisorLsaAnalysisResponse


class DMSDescribeFleetAdvisorLsaAnalysisResponse(BaseModel):
    Analysis: list[DMSFleetAdvisorLsaAnalysisResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
