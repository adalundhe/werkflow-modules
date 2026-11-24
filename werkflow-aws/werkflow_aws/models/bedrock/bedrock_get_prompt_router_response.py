from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_prompt_router_target_model import BedrockPromptRouterTargetModel
from .bedrock_routing_criteria import BedrockRoutingCriteria


class BedrockGetPromptRouterResponse(BaseModel):
    promptRouterName: StrictStr | None = None
    routingCriteria: BedrockRoutingCriteria | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    promptRouterArn: StrictStr | None = None
    models: list[BedrockPromptRouterTargetModel] | None = None
    fallbackModel: BedrockPromptRouterTargetModel | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
