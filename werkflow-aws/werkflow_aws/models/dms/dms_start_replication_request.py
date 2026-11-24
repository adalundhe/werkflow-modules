from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSStartReplicationRequest(BaseModel):
    ReplicationConfigArn: StrictStr
    StartReplicationType: StrictStr
    PremigrationAssessmentSettings: StrictStr | None = None
    CdcStartTime: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
