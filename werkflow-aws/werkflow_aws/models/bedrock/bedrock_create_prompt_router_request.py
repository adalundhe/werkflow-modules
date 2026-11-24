from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_prompt_router_target_model import BedrockPromptRouterTargetModel
from .bedrock_routing_criteria import BedrockRoutingCriteria
from .bedrock_tag import BedrockTag


class BedrockCreatePromptRouterRequest(BaseModel):
    promptRouterName: StrictStr
    models: list[BedrockPromptRouterTargetModel]
    routingCriteria: BedrockRoutingCriteria
    fallbackModel: BedrockPromptRouterTargetModel
    clientRequestToken: StrictStr | None = None
    description: StrictStr | None = None
    tags: list[BedrockTag] | None = None
