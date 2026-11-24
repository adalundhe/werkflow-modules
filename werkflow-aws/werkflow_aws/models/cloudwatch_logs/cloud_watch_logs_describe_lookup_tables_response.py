from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_lookup_table import CloudWatchLogsLookupTable


class CloudWatchLogsDescribeLookupTablesResponse(BaseModel):
    lookupTables: list[CloudWatchLogsLookupTable] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
