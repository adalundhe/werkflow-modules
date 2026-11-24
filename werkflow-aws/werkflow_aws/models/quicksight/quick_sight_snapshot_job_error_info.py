from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSnapshotJobErrorInfo(BaseModel):
    ErrorMessage: StrictStr | None = None
    ErrorType: StrictStr | None = None
