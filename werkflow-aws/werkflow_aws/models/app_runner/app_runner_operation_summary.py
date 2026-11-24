from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppRunnerOperationSummary(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    TargetArn: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
