from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaColumn(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Comment: StrictStr | None = None
