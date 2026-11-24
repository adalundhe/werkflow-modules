from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_parent_data_set import QuickSightParentDataSet


class QuickSightSourceTable(BaseModel):
    PhysicalTableId: StrictStr | None = None
    DataSet: QuickSightParentDataSet | None = None
