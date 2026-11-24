from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_data_source_introspection_result import AppSyncDataSourceIntrospectionResult


class AppSyncGetDataSourceIntrospectionResponse(BaseModel):
    introspectionId: StrictStr | None = None
    introspectionStatus: StrictStr | None = None
    introspectionStatusDetail: StrictStr | None = None
    introspectionResult: AppSyncDataSourceIntrospectionResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
