from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesStandbyWorkspacesProperties(BaseModel):
    StandbyWorkspaceId: StrictStr | None = None
    DataReplication: StrictStr | None = None
    RecoverySnapshotTime: datetime.datetime | StrictStr | None = None
