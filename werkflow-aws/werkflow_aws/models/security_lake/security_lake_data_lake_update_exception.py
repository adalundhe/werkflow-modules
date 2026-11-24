from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDataLakeUpdateException(BaseModel):
    code: StrictStr | None = None
    reason: StrictStr | None = None
