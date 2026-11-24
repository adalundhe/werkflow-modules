from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaSystemTableStatus(BaseModel):
    TableName: StrictStr | None = None
    Enabled: StrictBool | None = None
