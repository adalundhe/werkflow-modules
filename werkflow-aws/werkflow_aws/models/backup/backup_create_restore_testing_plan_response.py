from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateRestoreTestingPlanResponse(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    RestoreTestingPlanArn: StrictStr | None = None
    RestoreTestingPlanName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
