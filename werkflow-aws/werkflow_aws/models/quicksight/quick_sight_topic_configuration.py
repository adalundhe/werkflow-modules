from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_group_schema import QuickSightColumnGroupSchema
from .quick_sight_data_set_schema import QuickSightDataSetSchema


class QuickSightTopicConfiguration(BaseModel):
    Placeholder: StrictStr | None = None
    DataSetSchema: QuickSightDataSetSchema | None = None
    ColumnGroupSchemaList: list[QuickSightColumnGroupSchema] | None = None
