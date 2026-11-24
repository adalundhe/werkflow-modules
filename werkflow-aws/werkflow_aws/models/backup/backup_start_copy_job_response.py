from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class BackupStartCopyJobResponse(BaseModel):
    CopyJobId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    IsParent: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
