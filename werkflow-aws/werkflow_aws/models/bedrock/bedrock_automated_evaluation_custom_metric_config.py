from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_evaluation_custom_metric_source import BedrockAutomatedEvaluationCustomMetricSource
from .bedrock_custom_metric_evaluator_model_config import BedrockCustomMetricEvaluatorModelConfig


class BedrockAutomatedEvaluationCustomMetricConfig(BaseModel):
    customMetrics: list[BedrockAutomatedEvaluationCustomMetricSource] | None = None
    evaluatorModelConfig: BedrockCustomMetricEvaluatorModelConfig | None = None
