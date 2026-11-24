from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_reranking_metadata_selective_mode_configuration import BedrockRerankingMetadataSelectiveModeConfiguration


class BedrockMetadataConfigurationForReranking(BaseModel):
    selectionMode: StrictStr | None = None
    selectiveModeConfiguration: BedrockRerankingMetadataSelectiveModeConfiguration | None = None
