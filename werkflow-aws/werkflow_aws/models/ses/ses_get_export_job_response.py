from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_export_data_source import SESExportDataSource
from .ses_export_destination import SESExportDestination
from .ses_export_statistics import SESExportStatistics
from .ses_failure_info import SESFailureInfo


class SESGetExportJobResponse(BaseModel):
    JobId: StrictStr | None = None
    ExportSourceType: StrictStr | None = None
    JobStatus: StrictStr | None = None
    ExportDestination: SESExportDestination | None = None
    ExportDataSource: SESExportDataSource | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    CompletedTimestamp: datetime.datetime | StrictStr | None = None
    FailureInfo: SESFailureInfo | None = None
    Statistics: SESExportStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
