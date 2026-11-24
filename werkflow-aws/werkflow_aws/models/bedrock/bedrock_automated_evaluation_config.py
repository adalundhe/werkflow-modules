from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_evaluation_custom_metric_config import BedrockAutomatedEvaluationCustomMetricConfig
from .bedrock_evaluation_dataset_metric_config import BedrockEvaluationDatasetMetricConfig
from .bedrock_evaluator_model_config import BedrockEvaluatorModelConfig


class BedrockAutomatedEvaluationConfig(BaseModel):
    datasetMetricConfigs: list[BedrockEvaluationDatasetMetricConfig] | None = None
    evaluatorModelConfig: BedrockEvaluatorModelConfig | None = None
    customMetricConfig: BedrockAutomatedEvaluationCustomMetricConfig | None = None
