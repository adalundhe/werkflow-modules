from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteAccountDefaultProtectConfigurationResponse(BaseModel):
    DefaultProtectConfigurationArn: StrictStr | None = None
    DefaultProtectConfigurationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
