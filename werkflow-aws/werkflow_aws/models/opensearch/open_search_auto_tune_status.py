from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class OpenSearchAutoTuneStatus(BaseModel):
    CreationDate: datetime.datetime | StrictStr | None = None
    UpdateDate: datetime.datetime | StrictStr | None = None
    UpdateVersion: StrictInt | None = None
    State: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    PendingDeletion: StrictBool | None = None
