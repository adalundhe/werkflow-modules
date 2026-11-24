from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_citations_delta import BedrockRuntimeCitationsDelta
from .bedrock_runtime_image_block_delta import BedrockRuntimeImageBlockDelta
from .bedrock_runtime_reasoning_content_block_delta import BedrockRuntimeReasoningContentBlockDelta
from .bedrock_runtime_tool_result_block_delta import BedrockRuntimeToolResultBlockDelta
from .bedrock_runtime_tool_use_block_delta import BedrockRuntimeToolUseBlockDelta


class BedrockRuntimeContentBlockDelta(BaseModel):
    text: StrictStr | None = None
    toolUse: BedrockRuntimeToolUseBlockDelta | None = None
    toolResult: list[BedrockRuntimeToolResultBlockDelta] | None = None
    reasoningContent: BedrockRuntimeReasoningContentBlockDelta | None = None
    citation: BedrockRuntimeCitationsDelta | None = None
    image: BedrockRuntimeImageBlockDelta | None = None
