from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class Route53ChangeBatchSummary(BaseModel):
    ChangeId: StrictStr | None = None
    Operation: StrictStr | None = None
    SubmittedAt: datetime.datetime | StrictStr | None = None
    SubmittedBy: StrictStr | None = None
    RequestId: StrictStr | None = None
    Comment: StrictStr | None = None
    ChangeCount: StrictInt | None = None
