from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_latency_threshold import SageMakerModelLatencyThreshold


class SageMakerRecommendationJobStoppingConditions(BaseModel):
    MaxInvocations: StrictInt | None = None
    ModelLatencyThresholds: list[SageMakerModelLatencyThreshold] | None = None
    FlatInvocations: StrictStr | None = None
