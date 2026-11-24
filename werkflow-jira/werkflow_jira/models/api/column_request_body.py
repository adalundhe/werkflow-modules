from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ColumnRequestBody(BaseModel):
    columns: list[StrictStr] | None = None
