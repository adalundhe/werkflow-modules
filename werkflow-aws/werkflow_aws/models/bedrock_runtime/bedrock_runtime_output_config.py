from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_output_format import BedrockRuntimeOutputFormat


class BedrockRuntimeOutputConfig(BaseModel):
    textFormat: BedrockRuntimeOutputFormat | None = None
    effort: StrictStr | None = None
