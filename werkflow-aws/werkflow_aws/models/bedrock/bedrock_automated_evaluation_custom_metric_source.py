from __future__ import annotations
from pydantic import BaseModel
from .bedrock_custom_metric_definition import BedrockCustomMetricDefinition


class BedrockAutomatedEvaluationCustomMetricSource(BaseModel):
    customMetricDefinition: BedrockCustomMetricDefinition | None = None
