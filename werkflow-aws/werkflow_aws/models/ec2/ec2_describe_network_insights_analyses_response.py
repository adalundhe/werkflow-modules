from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_insights_analysis import EC2NetworkInsightsAnalysis


class EC2DescribeNetworkInsightsAnalysesResponse(BaseModel):
    NetworkInsightsAnalyses: list[EC2NetworkInsightsAnalysis] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
