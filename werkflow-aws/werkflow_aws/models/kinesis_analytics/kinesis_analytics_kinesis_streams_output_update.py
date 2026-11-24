from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisStreamsOutputUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
