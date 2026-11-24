from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTargetFilter(BaseModel):
    path: StrictStr | None = None
    values: list[StrictStr] | None = None
