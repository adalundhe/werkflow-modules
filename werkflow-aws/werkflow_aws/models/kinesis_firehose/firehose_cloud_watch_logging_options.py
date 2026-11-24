from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FirehoseCloudWatchLoggingOptions(BaseModel):
    Enabled: StrictBool | None = None
    LogGroupName: StrictStr | None = None
    LogStreamName: StrictStr | None = None
