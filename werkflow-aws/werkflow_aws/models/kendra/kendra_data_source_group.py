from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDataSourceGroup(BaseModel):
    GroupId: StrictStr
    DataSourceId: StrictStr
