from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_implicit_filter_configuration import BedrockImplicitFilterConfiguration
from .bedrock_retrieval_filter import BedrockRetrievalFilter
from .bedrock_vector_search_reranking_configuration import BedrockVectorSearchRerankingConfiguration


class BedrockKnowledgeBaseVectorSearchConfiguration(BaseModel):
    numberOfResults: StrictInt | None = None
    overrideSearchType: StrictStr | None = None
    filter: BedrockRetrievalFilter | None = None
    implicitFilterConfiguration: BedrockImplicitFilterConfiguration | None = None
    rerankingConfiguration: BedrockVectorSearchRerankingConfiguration | None = None
