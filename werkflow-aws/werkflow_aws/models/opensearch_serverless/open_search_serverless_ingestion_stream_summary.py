from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessIngestionStreamSummary(BaseModel):
    ingestionStreamId: StrictStr | None = None
    arn: StrictStr | None = None
    ingestionStreamName: StrictStr | None = None
    indexName: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
