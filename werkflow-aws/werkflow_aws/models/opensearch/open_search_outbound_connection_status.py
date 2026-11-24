from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchOutboundConnectionStatus(BaseModel):
    StatusCode: StrictStr | None = None
    Message: StrictStr | None = None
