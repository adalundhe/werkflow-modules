from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsInputLambdaProcessor(BaseModel):
    ResourceARN: StrictStr
