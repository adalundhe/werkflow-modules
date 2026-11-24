from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateTargetFilter(BaseModel):
    path: StrictStr | None = None
    values: list[StrictStr] | None = None
