from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubPatchSummary(BaseModel):
    Id: StrictStr | None = None
    InstalledCount: StrictInt | None = None
    MissingCount: StrictInt | None = None
    FailedCount: StrictInt | None = None
    InstalledOtherCount: StrictInt | None = None
    InstalledRejectedCount: StrictInt | None = None
    InstalledPendingReboot: StrictInt | None = None
    OperationStartTime: StrictStr | None = None
    OperationEndTime: StrictStr | None = None
    RebootOption: StrictStr | None = None
    Operation: StrictStr | None = None
