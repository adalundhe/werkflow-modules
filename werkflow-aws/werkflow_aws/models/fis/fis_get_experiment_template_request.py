from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISGetExperimentTemplateRequest(BaseModel):
    id: StrictStr
