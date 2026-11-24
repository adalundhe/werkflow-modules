from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdatePoolRequest(BaseModel):
    PoolId: StrictStr
    TwoWayEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    SharedRoutesEnabled: StrictBool | None = None
    DeletionProtectionEnabled: StrictBool | None = None
