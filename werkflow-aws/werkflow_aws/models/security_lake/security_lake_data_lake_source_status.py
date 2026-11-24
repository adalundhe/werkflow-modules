from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDataLakeSourceStatus(BaseModel):
    resource: StrictStr | None = None
    status: StrictStr | None = None
