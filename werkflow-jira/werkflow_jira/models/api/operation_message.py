from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OperationMessage(BaseModel):
    message: StrictStr | None = None
    statusCode: StrictInt | None = None
