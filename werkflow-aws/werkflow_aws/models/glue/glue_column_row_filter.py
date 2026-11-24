from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueColumnRowFilter(BaseModel):
    ColumnName: StrictStr | None = None
    RowFilterExpression: StrictStr | None = None
