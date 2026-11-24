from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_data_source import AppSyncDataSource


class AppSyncCreateDataSourceResponse(BaseModel):
    dataSource: AppSyncDataSource | None = None
    ResponseMetadata: dict[str, Any] | None = None
