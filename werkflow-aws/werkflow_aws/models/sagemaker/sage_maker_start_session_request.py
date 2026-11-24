from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartSessionRequest(BaseModel):
    ResourceIdentifier: StrictStr
