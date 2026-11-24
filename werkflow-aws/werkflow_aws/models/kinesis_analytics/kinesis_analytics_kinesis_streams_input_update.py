from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisStreamsInputUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
