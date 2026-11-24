from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_group_column_schema import QuickSightColumnGroupColumnSchema


class QuickSightColumnGroupSchema(BaseModel):
    Name: StrictStr | None = None
    ColumnGroupColumnSchemaList: list[QuickSightColumnGroupColumnSchema] | None = None
