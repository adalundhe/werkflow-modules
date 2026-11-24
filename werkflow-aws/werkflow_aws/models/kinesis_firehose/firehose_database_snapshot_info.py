from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .firehose_failure_description import FirehoseFailureDescription


class FirehoseDatabaseSnapshotInfo(BaseModel):
    Id: StrictStr | None = None
    Table: StrictStr | None = None
    RequestTimestamp: datetime.datetime | StrictStr | None = None
    RequestedBy: StrictStr | None = None
    Status: StrictStr | None = None
    FailureDescription: FirehoseFailureDescription | None = None
