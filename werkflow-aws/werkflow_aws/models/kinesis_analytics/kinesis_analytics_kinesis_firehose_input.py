from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisFirehoseInput(BaseModel):
    ResourceARN: StrictStr
