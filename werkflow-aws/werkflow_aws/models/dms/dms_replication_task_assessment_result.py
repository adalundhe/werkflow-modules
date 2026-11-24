from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSReplicationTaskAssessmentResult(BaseModel):
    ReplicationTaskIdentifier: StrictStr | None = None
    ReplicationTaskArn: StrictStr | None = None
    ReplicationTaskLastAssessmentDate: datetime.datetime | StrictStr | None = None
    AssessmentStatus: StrictStr | None = None
    AssessmentResultsFile: StrictStr | None = None
    AssessmentResults: StrictStr | None = None
    S3ObjectUrl: StrictStr | None = None
