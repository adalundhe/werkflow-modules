from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehosePutRecordBatchResponseEntry(BaseModel):
    RecordId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
