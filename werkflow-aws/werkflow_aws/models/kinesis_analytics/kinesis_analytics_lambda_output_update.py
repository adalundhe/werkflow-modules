from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsLambdaOutputUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
