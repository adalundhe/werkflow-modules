from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteExtractionDefinitionRequest(BaseModel):
    InstanceId: StrictStr
    ExtractionDefinitionId: StrictStr
