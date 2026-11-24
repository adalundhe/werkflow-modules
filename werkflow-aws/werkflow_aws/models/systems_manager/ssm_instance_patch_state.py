from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SSMInstancePatchState(BaseModel):
    InstanceId: StrictStr | None = None
    PatchGroup: StrictStr | None = None
    BaselineId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    InstallOverrideList: StrictStr | None = None
    OwnerInformation: StrictStr | None = None
    InstalledCount: StrictInt | None = None
    InstalledOtherCount: StrictInt | None = None
    InstalledPendingRebootCount: StrictInt | None = None
    InstalledRejectedCount: StrictInt | None = None
    MissingCount: StrictInt | None = None
    FailedCount: StrictInt | None = None
    UnreportedNotApplicableCount: StrictInt | None = None
    NotApplicableCount: StrictInt | None = None
    AvailableSecurityUpdateCount: StrictInt | None = None
    OperationStartTime: datetime.datetime | StrictStr | None = None
    OperationEndTime: datetime.datetime | StrictStr | None = None
    Operation: StrictStr | None = None
    LastNoRebootInstallOperationTime: datetime.datetime | StrictStr | None = None
    RebootOption: StrictStr | None = None
    CriticalNonCompliantCount: StrictInt | None = None
    SecurityNonCompliantCount: StrictInt | None = None
    OtherNonCompliantCount: StrictInt | None = None
