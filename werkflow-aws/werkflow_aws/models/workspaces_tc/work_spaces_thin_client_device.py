from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientDevice(BaseModel):
    id: StrictStr | None = None
    serialNumber: StrictStr | None = None
    name: StrictStr | None = None
    model: StrictStr | None = None
    environmentId: StrictStr | None = None
    status: StrictStr | None = None
    currentSoftwareSetId: StrictStr | None = None
    currentSoftwareSetVersion: StrictStr | None = None
    desiredSoftwareSetId: StrictStr | None = None
    pendingSoftwareSetId: StrictStr | None = None
    pendingSoftwareSetVersion: StrictStr | None = None
    softwareSetUpdateSchedule: StrictStr | None = None
    softwareSetComplianceStatus: StrictStr | None = None
    softwareSetUpdateStatus: StrictStr | None = None
    lastConnectedAt: datetime.datetime | StrictStr | None = None
    lastPostureAt: datetime.datetime | StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    arn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    lastUserId: StrictStr | None = None
