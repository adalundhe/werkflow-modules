from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_custom_model_deployment_summary import BedrockCustomModelDeploymentSummary


class BedrockListCustomModelDeploymentsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelDeploymentSummaries: list[BedrockCustomModelDeploymentSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
