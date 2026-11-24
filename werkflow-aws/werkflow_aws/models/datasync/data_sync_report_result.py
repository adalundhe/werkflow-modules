from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncReportResult(BaseModel):
    Status: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorDetail: StrictStr | None = None
