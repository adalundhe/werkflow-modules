from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisFirehoseOutput(BaseModel):
    ResourceARN: StrictStr
