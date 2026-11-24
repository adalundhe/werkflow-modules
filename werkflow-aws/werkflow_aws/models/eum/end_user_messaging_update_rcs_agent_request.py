from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateRcsAgentRequest(BaseModel):
    RcsAgentId: StrictStr
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
