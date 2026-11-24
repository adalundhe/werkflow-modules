from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppSyncLogConfig(BaseModel):
    fieldLogLevel: StrictStr | None = None
    cloudWatchLogsRoleArn: StrictStr | None = None
    excludeVerboseContent: StrictBool | None = None
