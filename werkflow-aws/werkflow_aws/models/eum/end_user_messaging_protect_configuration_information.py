from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingProtectConfigurationInformation(BaseModel):
    ProtectConfigurationArn: StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    AccountDefault: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
