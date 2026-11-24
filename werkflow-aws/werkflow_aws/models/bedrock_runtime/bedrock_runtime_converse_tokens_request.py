from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_document import BedrockRuntimeDocument
from .bedrock_runtime_message import BedrockRuntimeMessage
from .bedrock_runtime_system_content_block import BedrockRuntimeSystemContentBlock
from .bedrock_runtime_tool_configuration import BedrockRuntimeToolConfiguration


class BedrockRuntimeConverseTokensRequest(BaseModel):
    messages: list[BedrockRuntimeMessage] | None = None
    system: list[BedrockRuntimeSystemContentBlock] | None = None
    toolConfig: BedrockRuntimeToolConfiguration | None = None
    additionalModelRequestFields: BedrockRuntimeDocument | None = None
