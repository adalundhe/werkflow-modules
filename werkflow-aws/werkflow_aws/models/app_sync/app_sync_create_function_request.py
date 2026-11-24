from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_sync_runtime import AppSyncRuntime
from .app_sync_sync_config import AppSyncSyncConfig


class AppSyncCreateFunctionRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
    dataSourceName: StrictStr
    description: StrictStr | None = None
    requestMappingTemplate: StrictStr | None = None
    responseMappingTemplate: StrictStr | None = None
    functionVersion: StrictStr | None = None
    syncConfig: AppSyncSyncConfig | None = None
    maxBatchSize: StrictInt | None = None
    runtime: AppSyncRuntime | None = None
    code: StrictStr | None = None
