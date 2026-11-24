from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisAnalyticsStopApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    Force: StrictBool | None = None
