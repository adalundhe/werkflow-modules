from __future__ import annotations
from pydantic import BaseModel
from .bedrock_custom_metric_bedrock_evaluator_model import BedrockCustomMetricBedrockEvaluatorModel


class BedrockCustomMetricEvaluatorModelConfig(BaseModel):
    bedrockEvaluatorModels: list[BedrockCustomMetricBedrockEvaluatorModel] | None = None
