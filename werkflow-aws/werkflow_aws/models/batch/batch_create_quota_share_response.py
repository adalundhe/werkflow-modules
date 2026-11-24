from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchCreateQuotaShareResponse(BaseModel):
    quotaShareName: StrictStr | None = None
    quotaShareArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
