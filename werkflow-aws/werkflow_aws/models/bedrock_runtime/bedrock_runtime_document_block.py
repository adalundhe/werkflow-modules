from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_citations_config import BedrockRuntimeCitationsConfig
from .bedrock_runtime_document_source import BedrockRuntimeDocumentSource


class BedrockRuntimeDocumentBlock(BaseModel):
    format: StrictStr | None = None
    name: StrictStr | None = None
    source: BedrockRuntimeDocumentSource | None = None
    context: StrictStr | None = None
    citations: BedrockRuntimeCitationsConfig | None = None
