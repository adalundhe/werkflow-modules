from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_logical_table_source import QuickSightLogicalTableSource
from .quick_sight_transform_operation import QuickSightTransformOperation


class QuickSightLogicalTable(BaseModel):
    Alias: StrictStr | None = None
    DataTransforms: list[QuickSightTransformOperation] | None = None
    Source: QuickSightLogicalTableSource | None = None
