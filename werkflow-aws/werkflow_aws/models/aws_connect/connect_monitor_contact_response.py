from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectMonitorContactResponse(BaseModel):
    ContactId: StrictStr | None = None
    ContactArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
