from __future__ import annotations
from pydantic import BaseModel
from .bedrock_sage_maker_endpoint import BedrockSageMakerEndpoint


class BedrockEndpointConfig(BaseModel):
    sageMaker: BedrockSageMakerEndpoint | None = None
