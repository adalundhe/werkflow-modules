from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataSyncTaskExecutionResultDetail(BaseModel):
    PrepareDuration: StrictInt | None = None
    PrepareStatus: StrictStr | None = None
    TotalDuration: StrictInt | None = None
    TransferDuration: StrictInt | None = None
    TransferStatus: StrictStr | None = None
    VerifyDuration: StrictInt | None = None
    VerifyStatus: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorDetail: StrictStr | None = None
