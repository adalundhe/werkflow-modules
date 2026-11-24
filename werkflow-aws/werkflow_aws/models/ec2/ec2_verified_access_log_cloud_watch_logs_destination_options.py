from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VerifiedAccessLogCloudWatchLogsDestinationOptions(BaseModel):
    Enabled: StrictBool
    LogGroup: StrictStr | None = None
