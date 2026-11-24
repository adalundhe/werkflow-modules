from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISGetExperimentRequest(BaseModel):
    id: StrictStr
