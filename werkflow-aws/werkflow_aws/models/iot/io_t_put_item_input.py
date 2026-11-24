from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPutItemInput(BaseModel):
    tableName: StrictStr | None = None
