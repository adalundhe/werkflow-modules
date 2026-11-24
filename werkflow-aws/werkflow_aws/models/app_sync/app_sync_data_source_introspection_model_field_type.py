from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDataSourceIntrospectionModelFieldType(BaseModel):
    kind: StrictStr | None = None
    name: StrictStr | None = None
    type: AppSyncDataSourceIntrospectionModelFieldType | None = None
    values: list[StrictStr] | None = None
