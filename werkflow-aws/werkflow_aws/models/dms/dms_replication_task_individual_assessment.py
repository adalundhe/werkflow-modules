from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSReplicationTaskIndividualAssessment(BaseModel):
    ReplicationTaskIndividualAssessmentArn: StrictStr | None = None
    ReplicationTaskAssessmentRunArn: StrictStr | None = None
    IndividualAssessmentName: StrictStr | None = None
    Status: StrictStr | None = None
    ReplicationTaskIndividualAssessmentStartDate: datetime.datetime | StrictStr | None = None
