from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class FirehosePutRecordResponse(BaseModel):
    RecordId: StrictStr | None = None
    Encrypted: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
