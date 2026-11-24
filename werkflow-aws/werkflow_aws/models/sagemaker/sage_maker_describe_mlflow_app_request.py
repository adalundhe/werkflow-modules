from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeMlflowAppRequest(BaseModel):
    Arn: StrictStr
