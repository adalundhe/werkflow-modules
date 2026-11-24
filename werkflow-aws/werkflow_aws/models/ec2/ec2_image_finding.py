from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class EC2ImageFinding(BaseModel):
    FixAvailable: StrictBool | None = None
    Score: StrictFloat | StrictInt | None = None
    FirstObservedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Title: StrictStr | None = None
    Paths: list[StrictStr] | None = None
    SeverityLabel: StrictStr | None = None
    SnapshotId: StrictStr | None = None
