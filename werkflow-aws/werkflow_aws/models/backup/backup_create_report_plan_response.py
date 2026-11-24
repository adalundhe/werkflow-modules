from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateReportPlanResponse(BaseModel):
    ReportPlanName: StrictStr | None = None
    ReportPlanArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
