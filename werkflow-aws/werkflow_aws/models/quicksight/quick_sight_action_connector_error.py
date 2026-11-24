from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightActionConnectorError(BaseModel):
    Message: StrictStr | None = None
    Type: StrictStr | None = None
