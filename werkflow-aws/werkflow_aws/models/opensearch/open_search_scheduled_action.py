from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class OpenSearchScheduledAction(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Severity: StrictStr | None = None
    ScheduledTime: StrictInt | None = None
    Description: StrictStr | None = None
    ScheduledBy: StrictStr | None = None
    Status: StrictStr | None = None
    Mandatory: StrictBool | None = None
    Cancellable: StrictBool | None = None
