from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisCloudWatchLogsUpdateInput(BaseModel):
    Enabled: StrictBool
    LogGroupName: StrictStr | None = None
    LogStreamName: StrictStr | None = None
