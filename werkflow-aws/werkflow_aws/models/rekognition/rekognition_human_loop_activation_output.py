from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionHumanLoopActivationOutput(BaseModel):
    HumanLoopArn: StrictStr | None = None
    HumanLoopActivationReasons: list[StrictStr] | None = None
    HumanLoopActivationConditionsEvaluationResults: StrictStr | None = None
