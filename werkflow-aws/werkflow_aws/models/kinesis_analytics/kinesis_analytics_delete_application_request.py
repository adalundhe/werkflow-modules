from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDeleteApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    CreateTimestamp: datetime.datetime | StrictStr
