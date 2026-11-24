from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ecs_threshold_configuration import ECSThresholdConfiguration


class ECSDeploymentCircuitBreaker(BaseModel):
    enable: StrictBool | None = None
    rollback: StrictBool | None = None
    resetOnHealthyTask: StrictBool | None = None
    thresholdConfiguration: ECSThresholdConfiguration | None = None
