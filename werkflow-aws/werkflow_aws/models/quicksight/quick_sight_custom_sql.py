from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_input_column import QuickSightInputColumn


class QuickSightCustomSql(BaseModel):
    DataSourceArn: StrictStr | None = None
    Name: StrictStr | None = None
    SqlQuery: StrictStr | None = None
    Columns: list[QuickSightInputColumn] | None = None
