from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncEventLogConfig(BaseModel):
    logLevel: StrictStr | None = None
    cloudWatchLogsRoleArn: StrictStr | None = None
