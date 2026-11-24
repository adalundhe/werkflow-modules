from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchInboundConnectionStatus(BaseModel):
    StatusCode: StrictStr | None = None
    Message: StrictStr | None = None
