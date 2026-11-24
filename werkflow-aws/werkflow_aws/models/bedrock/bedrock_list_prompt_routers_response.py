from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_prompt_router_summary import BedrockPromptRouterSummary


class BedrockListPromptRoutersResponse(BaseModel):
    promptRouterSummaries: list[BedrockPromptRouterSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
