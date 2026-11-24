from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISStopExperimentRequest(BaseModel):
    id: StrictStr
