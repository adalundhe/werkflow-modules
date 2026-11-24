from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftSupportedOperation(BaseModel):
    OperationName: StrictStr | None = None
