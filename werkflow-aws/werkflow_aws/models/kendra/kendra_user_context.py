from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_group import KendraDataSourceGroup


class KendraUserContext(BaseModel):
    Token: StrictStr | None = None
    UserId: StrictStr | None = None
    Groups: list[StrictStr] | None = None
    DataSourceGroups: list[KendraDataSourceGroup] | None = None
