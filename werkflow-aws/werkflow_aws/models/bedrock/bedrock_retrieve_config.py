from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_knowledge_base_retrieval_configuration import BedrockKnowledgeBaseRetrievalConfiguration


class BedrockRetrieveConfig(BaseModel):
    knowledgeBaseId: StrictStr | None = None
    knowledgeBaseRetrievalConfiguration: BedrockKnowledgeBaseRetrievalConfiguration | None = None
