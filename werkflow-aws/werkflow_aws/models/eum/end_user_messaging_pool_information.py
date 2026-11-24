from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingPoolInformation(BaseModel):
    PoolArn: StrictStr | None = None
    PoolId: StrictStr | None = None
    Status: StrictStr | None = None
    MessageType: StrictStr | None = None
    TwoWayEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    SharedRoutesEnabled: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
