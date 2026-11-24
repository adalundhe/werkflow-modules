from __future__ import annotations
from pydantic import BaseModel
from .bedrock_field_for_reranking import BedrockFieldForReranking


class BedrockRerankingMetadataSelectiveModeConfiguration(BaseModel):
    fieldsToInclude: list[BedrockFieldForReranking] | None = None
    fieldsToExclude: list[BedrockFieldForReranking] | None = None
