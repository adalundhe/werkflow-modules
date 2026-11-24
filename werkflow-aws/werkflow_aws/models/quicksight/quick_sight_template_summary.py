from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTemplateSummary(BaseModel):
    Arn: StrictStr | None = None
    TemplateId: StrictStr | None = None
    Name: StrictStr | None = None
    LatestVersionNumber: StrictInt | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
