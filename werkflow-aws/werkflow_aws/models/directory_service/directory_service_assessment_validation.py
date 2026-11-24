from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceAssessmentValidation(BaseModel):
    Category: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    StatusCode: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdateDateTime: datetime.datetime | StrictStr | None = None
