from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_audio_block import BedrockRuntimeAudioBlock
from .bedrock_runtime_cache_point_block import BedrockRuntimeCachePointBlock
from .bedrock_runtime_citations_content_block import BedrockRuntimeCitationsContentBlock
from .bedrock_runtime_document_block import BedrockRuntimeDocumentBlock
from .bedrock_runtime_guardrail_converse_content_block import BedrockRuntimeGuardrailConverseContentBlock
from .bedrock_runtime_image_block import BedrockRuntimeImageBlock
from .bedrock_runtime_reasoning_content_block import BedrockRuntimeReasoningContentBlock
from .bedrock_runtime_search_result_block import BedrockRuntimeSearchResultBlock
from .bedrock_runtime_tool_addition_block import BedrockRuntimeToolAdditionBlock
from .bedrock_runtime_tool_removal_block import BedrockRuntimeToolRemovalBlock
from .bedrock_runtime_tool_result_block import BedrockRuntimeToolResultBlock
from .bedrock_runtime_tool_use_block import BedrockRuntimeToolUseBlock
from .bedrock_runtime_video_block import BedrockRuntimeVideoBlock


class BedrockRuntimeContentBlock(BaseModel):
    text: StrictStr | None = None
    image: BedrockRuntimeImageBlock | None = None
    document: BedrockRuntimeDocumentBlock | None = None
    video: BedrockRuntimeVideoBlock | None = None
    audio: BedrockRuntimeAudioBlock | None = None
    toolUse: BedrockRuntimeToolUseBlock | None = None
    toolResult: BedrockRuntimeToolResultBlock | None = None
    guardContent: BedrockRuntimeGuardrailConverseContentBlock | None = None
    cachePoint: BedrockRuntimeCachePointBlock | None = None
    reasoningContent: BedrockRuntimeReasoningContentBlock | None = None
    citationsContent: BedrockRuntimeCitationsContentBlock | None = None
    searchResult: BedrockRuntimeSearchResultBlock | None = None
    toolAddition: BedrockRuntimeToolAdditionBlock | None = None
    toolRemoval: BedrockRuntimeToolRemovalBlock | None = None
