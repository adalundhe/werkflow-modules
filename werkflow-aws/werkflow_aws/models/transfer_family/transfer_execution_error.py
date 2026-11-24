from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferExecutionError(BaseModel):
    Type: StrictStr | None = None
    Message: StrictStr | None = None
