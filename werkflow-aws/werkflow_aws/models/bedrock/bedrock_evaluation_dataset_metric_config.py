from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_dataset import BedrockEvaluationDataset


class BedrockEvaluationDatasetMetricConfig(BaseModel):
    taskType: StrictStr | None = None
    dataset: BedrockEvaluationDataset | None = None
    metricNames: list[StrictStr] | None = None
