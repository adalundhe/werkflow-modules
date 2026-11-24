from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingDeleteProtectConfigurationResponse(BaseModel):
    ProtectConfigurationArn: StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    AccountDefault: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
