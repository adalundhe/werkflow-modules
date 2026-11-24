from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractHumanLoopActivationOutput(BaseModel):
    HumanLoopArn: StrictStr | None = None
    HumanLoopActivationReasons: list[StrictStr] | None = None
    HumanLoopActivationConditionsEvaluationResults: StrictStr | None = None
