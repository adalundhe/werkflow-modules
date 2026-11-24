from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightSqlServerParameters(BaseModel):
    Host: StrictStr | None = None
    Port: StrictInt | None = None
    Database: StrictStr | None = None
