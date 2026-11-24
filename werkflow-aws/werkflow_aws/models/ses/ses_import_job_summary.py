from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ses_import_destination import SESImportDestination


class SESImportJobSummary(BaseModel):
    JobId: StrictStr | None = None
    ImportDestination: SESImportDestination | None = None
    JobStatus: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ProcessedRecordsCount: StrictInt | None = None
    FailedRecordsCount: StrictInt | None = None
