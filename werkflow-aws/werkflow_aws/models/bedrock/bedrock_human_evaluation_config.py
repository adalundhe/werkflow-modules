from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluation_dataset_metric_config import BedrockEvaluationDatasetMetricConfig
from .bedrock_human_evaluation_custom_metric import BedrockHumanEvaluationCustomMetric
from .bedrock_human_workflow_config import BedrockHumanWorkflowConfig


class BedrockHumanEvaluationConfig(BaseModel):
    humanWorkflowConfig: BedrockHumanWorkflowConfig | None = None
    customMetrics: list[BedrockHumanEvaluationCustomMetric] | None = None
    datasetMetricConfigs: list[BedrockEvaluationDatasetMetricConfig] | None = None
