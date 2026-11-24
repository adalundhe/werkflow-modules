from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisFirehoseInputUpdate(BaseModel):
    ResourceARNUpdate: StrictStr
