from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelRequest(BaseModel):
    ModelName: StrictStr
