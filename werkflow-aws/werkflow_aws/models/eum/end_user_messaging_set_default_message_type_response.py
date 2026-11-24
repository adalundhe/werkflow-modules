from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingSetDefaultMessageTypeResponse(BaseModel):
    ConfigurationSetArn: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    MessageType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
