from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelRequest(BaseModel):
    ModelName: StrictStr
