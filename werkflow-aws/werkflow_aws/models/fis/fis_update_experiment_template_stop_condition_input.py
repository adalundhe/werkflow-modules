from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISUpdateExperimentTemplateStopConditionInput(BaseModel):
    source: StrictStr
    value: StrictStr | None = None
