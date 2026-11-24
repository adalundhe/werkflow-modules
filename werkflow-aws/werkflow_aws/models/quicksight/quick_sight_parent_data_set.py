from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_input_column import QuickSightInputColumn


class QuickSightParentDataSet(BaseModel):
    DataSetArn: StrictStr | None = None
    InputColumns: list[QuickSightInputColumn] | None = None
