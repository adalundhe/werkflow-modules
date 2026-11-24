from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_import_filter import CloudWatchLogsImportFilter
from .cloud_watch_logs_import_statistics import CloudWatchLogsImportStatistics


class CloudWatchLogsImport(BaseModel):
    importId: StrictStr | None = None
    importSourceArn: StrictStr | None = None
    importStatus: StrictStr | None = None
    importDestinationArn: StrictStr | None = None
    importStatistics: CloudWatchLogsImportStatistics | None = None
    importFilter: CloudWatchLogsImportFilter | None = None
    creationTime: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
    errorMessage: StrictStr | None = None
