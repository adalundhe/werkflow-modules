from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisFirehoseOutputUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
