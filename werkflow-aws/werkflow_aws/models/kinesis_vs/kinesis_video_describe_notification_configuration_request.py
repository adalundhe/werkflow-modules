from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDescribeNotificationConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
