from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListAssessmentFindingsRequest(BaseModel):
    AssessmentArn: StrictStr
    ClusterArn: StrictStr
    Category: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Severity: StrictStr | None = None
