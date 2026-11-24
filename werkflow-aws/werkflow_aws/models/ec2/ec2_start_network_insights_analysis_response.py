from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_network_insights_analysis import EC2NetworkInsightsAnalysis


class EC2StartNetworkInsightsAnalysisResponse(BaseModel):
    NetworkInsightsAnalysis: EC2NetworkInsightsAnalysis | None = None
    ResponseMetadata: dict[str, Any] | None = None
