from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateTieringConfigurationResponse(BaseModel):
    TieringConfigurationArn: StrictStr | None = None
    TieringConfigurationName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
