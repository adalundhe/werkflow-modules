from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeregisterJobDefinitionRequest(BaseModel):
    jobDefinition: StrictStr
