from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeregisterTaskDefinitionRequest(BaseModel):
    taskDefinition: StrictStr
