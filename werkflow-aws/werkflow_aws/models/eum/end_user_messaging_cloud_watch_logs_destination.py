from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingCloudWatchLogsDestination(BaseModel):
    IamRoleArn: StrictStr | None = None
    LogGroupArn: StrictStr | None = None
