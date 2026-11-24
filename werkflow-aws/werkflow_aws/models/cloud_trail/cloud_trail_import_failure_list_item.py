from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudTrailImportFailureListItem(BaseModel):
    Location: StrictStr | None = None
    Status: StrictStr | None = None
    ErrorType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
