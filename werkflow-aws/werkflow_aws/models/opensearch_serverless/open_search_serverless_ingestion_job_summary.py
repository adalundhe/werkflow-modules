from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessIngestionJobSummary(BaseModel):
    ingestionJobId: StrictStr | None = None
    arn: StrictStr | None = None
    ingestionJobName: StrictStr | None = None
    indexName: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
