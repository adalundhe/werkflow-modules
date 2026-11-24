from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluation_model_config_summary import BedrockEvaluationModelConfigSummary
from .bedrock_evaluation_rag_config_summary import BedrockEvaluationRagConfigSummary


class BedrockEvaluationInferenceConfigSummary(BaseModel):
    modelConfigSummary: BedrockEvaluationModelConfigSummary | None = None
    ragConfigSummary: BedrockEvaluationRagConfigSummary | None = None
