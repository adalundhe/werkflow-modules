from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MSKAssessmentInfo(BaseModel):
    AssessmentArn: StrictStr | None = None
    AssessmentType: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
