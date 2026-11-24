from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ses_failure_info import SESFailureInfo
from .ses_import_data_source import SESImportDataSource
from .ses_import_destination import SESImportDestination


class SESGetImportJobResponse(BaseModel):
    JobId: StrictStr | None = None
    ImportDestination: SESImportDestination | None = None
    ImportDataSource: SESImportDataSource | None = None
    FailureInfo: SESFailureInfo | None = None
    JobStatus: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    CompletedTimestamp: datetime.datetime | StrictStr | None = None
    ProcessedRecordsCount: StrictInt | None = None
    FailedRecordsCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
