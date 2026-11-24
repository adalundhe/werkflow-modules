from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_sync_data_source_introspection_model_field_type import AppSyncDataSourceIntrospectionModelFieldType


class AppSyncDataSourceIntrospectionModelField(BaseModel):
    name: StrictStr | None = None
    type: AppSyncDataSourceIntrospectionModelFieldType | None = None
    length: StrictInt | None = None
