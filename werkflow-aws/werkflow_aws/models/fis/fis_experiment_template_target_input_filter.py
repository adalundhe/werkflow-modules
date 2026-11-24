from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateTargetInputFilter(BaseModel):
    path: StrictStr
    values: list[StrictStr]
