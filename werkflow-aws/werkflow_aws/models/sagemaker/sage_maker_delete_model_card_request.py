from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelCardRequest(BaseModel):
    ModelCardName: StrictStr
