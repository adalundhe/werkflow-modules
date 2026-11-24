from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KinesisPutRecordResponse(BaseModel):
    ShardId: StrictStr | None = None
    SequenceNumber: StrictStr | None = None
    EncryptionType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
