from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_endpoint_config import BedrockEndpointConfig


class BedrockUpdateMarketplaceModelEndpointRequest(BaseModel):
    endpointArn: StrictStr
    endpointConfig: BedrockEndpointConfig
    clientRequestToken: StrictStr | None = None
