from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerParameter(BaseModel):
    Name: StrictStr
    Value: StrictStr
