from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_performance_configuration import BedrockPerformanceConfiguration


class BedrockEvaluationBedrockModel(BaseModel):
    modelIdentifier: StrictStr | None = None
    inferenceParams: StrictStr | None = None
    performanceConfig: BedrockPerformanceConfiguration | None = None
