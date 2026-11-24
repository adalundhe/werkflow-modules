from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluation_precomputed_rag_source_config import BedrockEvaluationPrecomputedRagSourceConfig
from .bedrock_knowledge_base_config import BedrockKnowledgeBaseConfig


class BedrockRAGConfig(BaseModel):
    knowledgeBaseConfig: BedrockKnowledgeBaseConfig | None = None
    precomputedRagSourceConfig: BedrockEvaluationPrecomputedRagSourceConfig | None = None
