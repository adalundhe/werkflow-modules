from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_metadata_configuration_for_reranking import BedrockMetadataConfigurationForReranking
from .bedrock_vector_search_bedrock_reranking_model_configuration import BedrockVectorSearchBedrockRerankingModelConfiguration


class BedrockVectorSearchBedrockRerankingConfiguration(BaseModel):
    modelConfiguration: BedrockVectorSearchBedrockRerankingModelConfiguration | None = None
    numberOfRerankedResults: StrictInt | None = None
    metadataConfiguration: BedrockMetadataConfigurationForReranking | None = None
