from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightSelfUpgradeRequestDetail(BaseModel):
    UpgradeRequestId: StrictStr | None = None
    UserName: StrictStr | None = None
    OriginalRole: StrictStr | None = None
    RequestedRole: StrictStr | None = None
    RequestNote: StrictStr | None = None
    CreationTime: StrictInt | None = None
    RequestStatus: StrictStr | None = None
    lastUpdateAttemptTime: StrictInt | None = None
    lastUpdateFailureReason: StrictStr | None = None
