from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateTicketV2Response(BaseModel):
    TicketId: StrictStr | None = None
    TicketSrcUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
