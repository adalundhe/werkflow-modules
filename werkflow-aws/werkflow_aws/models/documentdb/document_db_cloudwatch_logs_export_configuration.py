from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBCloudwatchLogsExportConfiguration(BaseModel):
    EnableLogTypes: list[StrictStr] | None = None
    DisableLogTypes: list[StrictStr] | None = None
