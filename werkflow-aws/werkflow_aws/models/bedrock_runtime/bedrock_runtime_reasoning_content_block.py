from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes
from .bedrock_runtime_reasoning_text_block import BedrockRuntimeReasoningTextBlock


class BedrockRuntimeReasoningContentBlock(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    reasoningText: BedrockRuntimeReasoningTextBlock | None = None
    redactedContent: StrictBytes | Any | None = None
