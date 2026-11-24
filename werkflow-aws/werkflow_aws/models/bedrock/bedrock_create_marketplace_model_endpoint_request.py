from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .bedrock_endpoint_config import BedrockEndpointConfig
from .bedrock_tag import BedrockTag


class BedrockCreateMarketplaceModelEndpointRequest(BaseModel):
    modelSourceIdentifier: StrictStr
    endpointConfig: BedrockEndpointConfig
    endpointName: StrictStr
    acceptEula: StrictBool | None = None
    clientRequestToken: StrictStr | None = None
    tags: list[BedrockTag] | None = None
