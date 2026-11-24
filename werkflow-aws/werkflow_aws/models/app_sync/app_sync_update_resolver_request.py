from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .app_sync_caching_config import AppSyncCachingConfig
from .app_sync_pipeline_config import AppSyncPipelineConfig
from .app_sync_runtime import AppSyncRuntime
from .app_sync_sync_config import AppSyncSyncConfig


class AppSyncUpdateResolverRequest(BaseModel):
    apiId: StrictStr
    typeName: StrictStr
    fieldName: StrictStr
    dataSourceName: StrictStr | None = None
    requestMappingTemplate: StrictStr | None = None
    responseMappingTemplate: StrictStr | None = None
    kind: Literal['UNIT', 'PIPELINE'] | None = None
    pipelineConfig: AppSyncPipelineConfig | None = None
    syncConfig: AppSyncSyncConfig | None = None
    cachingConfig: AppSyncCachingConfig | None = None
    maxBatchSize: StrictInt | None = None
    runtime: AppSyncRuntime | None = None
    code: StrictStr | None = None
    metricsConfig: Literal['ENABLED', 'DISABLED'] | None = None
