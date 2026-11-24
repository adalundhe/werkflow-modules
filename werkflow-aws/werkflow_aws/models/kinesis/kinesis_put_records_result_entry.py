from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisPutRecordsResultEntry(BaseModel):
    SequenceNumber: StrictStr | None = None
    ShardId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
