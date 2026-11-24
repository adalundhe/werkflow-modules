from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_network_insights_path import EC2NetworkInsightsPath


class EC2CreateNetworkInsightsPathResponse(BaseModel):
    NetworkInsightsPath: EC2NetworkInsightsPath | None = None
    ResponseMetadata: dict[str, Any] | None = None
