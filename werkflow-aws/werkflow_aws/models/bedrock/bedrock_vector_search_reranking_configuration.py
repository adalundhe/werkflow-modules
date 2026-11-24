from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_vector_search_bedrock_reranking_configuration import BedrockVectorSearchBedrockRerankingConfiguration


class BedrockVectorSearchRerankingConfiguration(BaseModel):
    type: StrictStr | None = None
    bedrockRerankingConfiguration: BedrockVectorSearchBedrockRerankingConfiguration | None = None
