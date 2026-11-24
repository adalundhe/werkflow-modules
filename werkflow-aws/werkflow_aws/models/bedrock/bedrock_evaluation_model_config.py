from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluation_bedrock_model import BedrockEvaluationBedrockModel
from .bedrock_evaluation_precomputed_inference_source import BedrockEvaluationPrecomputedInferenceSource


class BedrockEvaluationModelConfig(BaseModel):
    bedrockModel: BedrockEvaluationBedrockModel | None = None
    precomputedInferenceSource: BedrockEvaluationPrecomputedInferenceSource | None = None
