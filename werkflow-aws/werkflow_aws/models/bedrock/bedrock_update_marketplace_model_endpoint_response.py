from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_marketplace_model_endpoint import BedrockMarketplaceModelEndpoint


class BedrockUpdateMarketplaceModelEndpointResponse(BaseModel):
    marketplaceModelEndpoint: BedrockMarketplaceModelEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
