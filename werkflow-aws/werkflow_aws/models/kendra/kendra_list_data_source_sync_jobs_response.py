from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_data_source_sync_job import KendraDataSourceSyncJob


class KendraListDataSourceSyncJobsResponse(BaseModel):
    History: list[KendraDataSourceSyncJob] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
