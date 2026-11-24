from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_data_source_sync_job import QBusinessDataSourceSyncJob


class QBusinessListDataSourceSyncJobsResponse(BaseModel):
    history: list[QBusinessDataSourceSyncJob] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
