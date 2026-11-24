from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateStopCondition(BaseModel):
    source: StrictStr | None = None
    value: StrictStr | None = None
