from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupDescribeGlobalSettingsResponse(BaseModel):
    GlobalSettings: dict[StrictStr, StrictStr] | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
