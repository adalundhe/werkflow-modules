from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetEbsEncryptionByDefaultResponse(BaseModel):
    EbsEncryptionByDefault: StrictBool | None = None
    SseType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
