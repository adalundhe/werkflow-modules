from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetOperationRequest(BaseModel):
    operationId: StrictStr
