from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_rds_http_endpoint_config import AppSyncRdsHttpEndpointConfig


class AppSyncRelationalDatabaseDataSourceConfig(BaseModel):
    relationalDatabaseSourceType: StrictStr | None = None
    rdsHttpEndpointConfig: AppSyncRdsHttpEndpointConfig | None = None
