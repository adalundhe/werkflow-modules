from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDistributeDataset(BaseModel):
    Arn: StrictStr
