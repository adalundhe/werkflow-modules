from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_input_column import QuickSightInputColumn


class QuickSightRelationalTable(BaseModel):
    DataSourceArn: StrictStr | None = None
    Catalog: StrictStr | None = None
    Schema: StrictStr | None = None
    Name: StrictStr | None = None
    InputColumns: list[QuickSightInputColumn] | None = None
