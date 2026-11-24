from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_citation import BedrockRuntimeCitation
from .bedrock_runtime_citation_generated_content import BedrockRuntimeCitationGeneratedContent


class BedrockRuntimeCitationsContentBlock(BaseModel):
    content: list[BedrockRuntimeCitationGeneratedContent] | None = None
    citations: list[BedrockRuntimeCitation] | None = None
