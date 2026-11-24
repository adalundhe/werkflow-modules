from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDashboardValidationMessage(BaseModel):
    DataPath: StrictStr | None = None
    Message: StrictStr | None = None
