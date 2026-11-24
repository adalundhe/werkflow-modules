from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateNotifyConfigurationResponse(BaseModel):
    NotifyConfigurationArn: StrictStr | None = None
    NotifyConfigurationId: StrictStr | None = None
    DisplayName: StrictStr | None = None
    UseCase: StrictStr | None = None
    DefaultTemplateId: StrictStr | None = None
    PoolId: StrictStr | None = None
    EnabledCountries: list[StrictStr] | None = None
    EnabledChannels: list[StrictStr] | None = None
    Tier: StrictStr | None = None
    TierUpgradeStatus: StrictStr | None = None
    Status: StrictStr | None = None
    RejectionReason: StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
