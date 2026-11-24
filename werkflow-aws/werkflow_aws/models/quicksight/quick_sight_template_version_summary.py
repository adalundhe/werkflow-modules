from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTemplateVersionSummary(BaseModel):
    Arn: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
