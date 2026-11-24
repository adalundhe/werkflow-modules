from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_sync_delta_sync_config import AppSyncDeltaSyncConfig


class AppSyncDynamodbDataSourceConfig(BaseModel):
    tableName: StrictStr | None = None
    awsRegion: StrictStr | None = None
    useCallerCredentials: StrictBool | None = None
    deltaSyncConfig: AppSyncDeltaSyncConfig | None = None
    versioned: StrictBool | None = None
