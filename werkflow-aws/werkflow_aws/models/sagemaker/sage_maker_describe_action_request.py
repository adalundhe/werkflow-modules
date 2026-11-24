from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeActionRequest(BaseModel):
    ActionName: StrictStr
