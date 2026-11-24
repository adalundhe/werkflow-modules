from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateRcsAgentResponse(BaseModel):
    RcsAgentArn: StrictStr | None = None
    RcsAgentId: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    TwoWayEnabled: StrictBool | None = None
    TwoWayMediaS3BucketName: StrictStr | None = None
    TwoWayMediaS3KeyPrefix: StrictStr | None = None
    TwoWayMediaS3Role: StrictStr | None = None
    TwoWayRcsEventsEnabled: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
