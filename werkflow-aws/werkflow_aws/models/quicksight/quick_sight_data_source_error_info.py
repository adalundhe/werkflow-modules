from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSourceErrorInfo(BaseModel):
    Type: StrictStr | None = None
    Message: StrictStr | None = None
