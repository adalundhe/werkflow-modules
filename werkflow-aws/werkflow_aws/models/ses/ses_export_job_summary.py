from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESExportJobSummary(BaseModel):
    JobId: StrictStr | None = None
    ExportSourceType: StrictStr | None = None
    JobStatus: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    CompletedTimestamp: datetime.datetime | StrictStr | None = None
