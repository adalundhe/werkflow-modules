from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_marketplace_model_endpoint_summary import BedrockMarketplaceModelEndpointSummary


class BedrockListMarketplaceModelEndpointsResponse(BaseModel):
    marketplaceModelEndpoints: list[BedrockMarketplaceModelEndpointSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
