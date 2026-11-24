from __future__ import annotations
from pydantic import BaseModel
from .app_sync_rds_data_api_config import AppSyncRdsDataApiConfig


class AppSyncStartDataSourceIntrospectionRequest(BaseModel):
    rdsDataApiConfig: AppSyncRdsDataApiConfig | None = None
