from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2EnableFastSnapshotRestoreSuccessItem(BaseModel):
    SnapshotId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    State: StrictStr | None = None
    StateTransitionReason: StrictStr | None = None
    OwnerId: StrictStr | None = None
    OwnerAlias: StrictStr | None = None
    EnablingTime: datetime.datetime | StrictStr | None = None
    OptimizingTime: datetime.datetime | StrictStr | None = None
    EnabledTime: datetime.datetime | StrictStr | None = None
    DisablingTime: datetime.datetime | StrictStr | None = None
    DisabledTime: datetime.datetime | StrictStr | None = None
