from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_data_source_introspection_model_field import AppSyncDataSourceIntrospectionModelField
from .app_sync_data_source_introspection_model_index import AppSyncDataSourceIntrospectionModelIndex


class AppSyncDataSourceIntrospectionModel(BaseModel):
    name: StrictStr | None = None
    fields: list[AppSyncDataSourceIntrospectionModelField] | None = None
    primaryKey: AppSyncDataSourceIntrospectionModelIndex | None = None
    indexes: list[AppSyncDataSourceIntrospectionModelIndex] | None = None
    sdl: StrictStr | None = None
