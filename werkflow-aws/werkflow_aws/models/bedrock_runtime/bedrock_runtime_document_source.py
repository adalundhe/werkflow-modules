from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .bedrock_runtime_document_content_block import BedrockRuntimeDocumentContentBlock
from .bedrock_runtime_s3_location import BedrockRuntimeS3Location


class BedrockRuntimeDocumentSource(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    bytes: StrictBytes | Any | None = None
    s3Location: BedrockRuntimeS3Location | None = None
    text: StrictStr | None = None
    content: list[BedrockRuntimeDocumentContentBlock] | None = None
