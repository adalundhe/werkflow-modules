from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsPendingCloudWatchLogsExports(BaseModel):
    LogTypesToEnable: list[StrictStr] | None = None
    LogTypesToDisable: list[StrictStr] | None = None
