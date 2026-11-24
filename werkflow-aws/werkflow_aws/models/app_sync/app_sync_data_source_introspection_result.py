from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_data_source_introspection_model import AppSyncDataSourceIntrospectionModel


class AppSyncDataSourceIntrospectionResult(BaseModel):
    models: list[AppSyncDataSourceIntrospectionModel] | None = None
    nextToken: StrictStr | None = None
