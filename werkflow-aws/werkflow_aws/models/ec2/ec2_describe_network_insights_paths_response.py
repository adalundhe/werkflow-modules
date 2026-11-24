from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_insights_path import EC2NetworkInsightsPath


class EC2DescribeNetworkInsightsPathsResponse(BaseModel):
    NetworkInsightsPaths: list[EC2NetworkInsightsPath] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
