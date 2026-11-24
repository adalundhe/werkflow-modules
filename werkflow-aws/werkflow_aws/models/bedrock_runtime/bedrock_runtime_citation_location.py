from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_document_char_location import BedrockRuntimeDocumentCharLocation
from .bedrock_runtime_document_chunk_location import BedrockRuntimeDocumentChunkLocation
from .bedrock_runtime_document_page_location import BedrockRuntimeDocumentPageLocation
from .bedrock_runtime_search_result_location import BedrockRuntimeSearchResultLocation
from .bedrock_runtime_web_location import BedrockRuntimeWebLocation


class BedrockRuntimeCitationLocation(BaseModel):
    web: BedrockRuntimeWebLocation | None = None
    documentChar: BedrockRuntimeDocumentCharLocation | None = None
    documentPage: BedrockRuntimeDocumentPageLocation | None = None
    documentChunk: BedrockRuntimeDocumentChunkLocation | None = None
    searchResultLocation: BedrockRuntimeSearchResultLocation | None = None
