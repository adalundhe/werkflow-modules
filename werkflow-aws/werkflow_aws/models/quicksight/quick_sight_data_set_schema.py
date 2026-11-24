from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_schema import QuickSightColumnSchema


class QuickSightDataSetSchema(BaseModel):
    ColumnSchemaList: list[QuickSightColumnSchema] | None = None
