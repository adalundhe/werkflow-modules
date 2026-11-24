from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UserColumnRequestBody(BaseModel):
    columns: list[StrictStr] | None = None
