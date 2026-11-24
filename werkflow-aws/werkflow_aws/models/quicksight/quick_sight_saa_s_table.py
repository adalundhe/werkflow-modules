from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_input_column import QuickSightInputColumn
from .quick_sight_table_path_element import QuickSightTablePathElement


class QuickSightSaaSTable(BaseModel):
    DataSourceArn: StrictStr | None = None
    TablePath: list[QuickSightTablePathElement] | None = None
    InputColumns: list[QuickSightInputColumn] | None = None
