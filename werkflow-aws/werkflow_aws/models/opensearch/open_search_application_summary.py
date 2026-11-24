from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchApplicationSummary(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    name: StrictStr | None = None
    endpoint: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
