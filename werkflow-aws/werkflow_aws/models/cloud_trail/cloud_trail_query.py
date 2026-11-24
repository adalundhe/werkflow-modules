from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudTrailQuery(BaseModel):
    QueryId: StrictStr | None = None
    QueryStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
