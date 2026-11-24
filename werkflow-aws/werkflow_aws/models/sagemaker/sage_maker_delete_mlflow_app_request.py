from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteMlflowAppRequest(BaseModel):
    Arn: StrictStr
