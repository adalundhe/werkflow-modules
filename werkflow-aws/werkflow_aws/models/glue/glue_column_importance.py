from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueColumnImportance(BaseModel):
    ColumnName: StrictStr | None = None
    Importance: StrictFloat | StrictInt | None = None
