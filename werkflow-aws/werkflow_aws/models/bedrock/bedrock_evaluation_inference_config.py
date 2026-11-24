from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluation_model_config import BedrockEvaluationModelConfig
from .bedrock_rag_config import BedrockRAGConfig


class BedrockEvaluationInferenceConfig(BaseModel):
    models: list[BedrockEvaluationModelConfig] | None = None
    ragConfigs: list[BedrockRAGConfig] | None = None
