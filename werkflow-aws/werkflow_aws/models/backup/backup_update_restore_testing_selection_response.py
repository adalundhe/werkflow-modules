from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupUpdateRestoreTestingSelectionResponse(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    RestoreTestingPlanArn: StrictStr | None = None
    RestoreTestingPlanName: StrictStr | None = None
    RestoreTestingSelectionName: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
