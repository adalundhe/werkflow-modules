from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDataSourceIntrospectionModelIndex(BaseModel):
    name: StrictStr | None = None
    fields: list[StrictStr] | None = None
