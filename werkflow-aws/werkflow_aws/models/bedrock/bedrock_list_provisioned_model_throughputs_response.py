from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_provisioned_model_summary import BedrockProvisionedModelSummary


class BedrockListProvisionedModelThroughputsResponse(BaseModel):
    nextToken: StrictStr | None = None
    provisionedModelSummaries: list[BedrockProvisionedModelSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
