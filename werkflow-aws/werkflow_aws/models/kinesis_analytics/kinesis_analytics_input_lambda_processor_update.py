from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsInputLambdaProcessorUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
