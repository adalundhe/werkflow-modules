from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeAlgorithmRequest(BaseModel):
    AlgorithmName: StrictStr
