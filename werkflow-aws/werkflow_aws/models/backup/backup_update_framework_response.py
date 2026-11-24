from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupUpdateFrameworkResponse(BaseModel):
    FrameworkName: StrictStr | None = None
    FrameworkArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
