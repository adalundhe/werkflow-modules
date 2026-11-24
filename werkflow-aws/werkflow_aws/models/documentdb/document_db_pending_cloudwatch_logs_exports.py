from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBPendingCloudwatchLogsExports(BaseModel):
    LogTypesToEnable: list[StrictStr] | None = None
    LogTypesToDisable: list[StrictStr] | None = None
