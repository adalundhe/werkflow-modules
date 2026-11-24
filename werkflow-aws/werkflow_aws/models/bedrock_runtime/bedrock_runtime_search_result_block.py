from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_citations_config import BedrockRuntimeCitationsConfig
from .bedrock_runtime_search_result_content_block import BedrockRuntimeSearchResultContentBlock


class BedrockRuntimeSearchResultBlock(BaseModel):
    source: StrictStr | None = None
    title: StrictStr | None = None
    content: list[BedrockRuntimeSearchResultContentBlock] | None = None
    citations: BedrockRuntimeCitationsConfig | None = None
