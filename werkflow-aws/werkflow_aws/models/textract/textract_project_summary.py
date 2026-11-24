from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TextractProjectSummary(BaseModel):
    ProjectArn: StrictStr | None = None
    ProjectName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
