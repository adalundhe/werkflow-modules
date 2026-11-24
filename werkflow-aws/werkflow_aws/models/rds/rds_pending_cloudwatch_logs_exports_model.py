from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSPendingCloudwatchLogsExportsModel(BaseModel):
    LogTypesToEnable: list[StrictStr] | None = None
    LogTypesToDisable: list[StrictStr] | None = None
