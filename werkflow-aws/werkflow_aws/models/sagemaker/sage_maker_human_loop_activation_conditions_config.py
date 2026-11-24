from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHumanLoopActivationConditionsConfig(BaseModel):
    HumanLoopActivationConditions: StrictStr | None = None
