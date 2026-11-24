from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_sync_runtime import AppSyncRuntime
from .app_sync_sync_config import AppSyncSyncConfig


class AppSyncFunctionConfiguration(BaseModel):
    functionId: StrictStr | None = None
    functionArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    dataSourceName: StrictStr | None = None
    requestMappingTemplate: StrictStr | None = None
    responseMappingTemplate: StrictStr | None = None
    functionVersion: StrictStr | None = None
    syncConfig: AppSyncSyncConfig | None = None
    maxBatchSize: StrictInt | None = None
    runtime: AppSyncRuntime | None = None
    code: StrictStr | None = None
