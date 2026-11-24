from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .bedrock_runtime_tool_input_schema import BedrockRuntimeToolInputSchema


class BedrockRuntimeToolSpecification(BaseModel):
    name: StrictStr
    inputSchema: BedrockRuntimeToolInputSchema
    description: StrictStr | None = None
    strict: StrictBool | None = None
