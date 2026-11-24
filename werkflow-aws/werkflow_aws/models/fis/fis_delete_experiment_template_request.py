from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISDeleteExperimentTemplateRequest(BaseModel):
    id: StrictStr
