from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_data_source import AppSyncDataSource


class AppSyncListDataSourcesResponse(BaseModel):
    dataSources: list[AppSyncDataSource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
