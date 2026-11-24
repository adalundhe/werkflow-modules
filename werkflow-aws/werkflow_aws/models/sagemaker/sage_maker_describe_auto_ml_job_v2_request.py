from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeAutoMLJobV2Request(BaseModel):
    AutoMLJobName: StrictStr
