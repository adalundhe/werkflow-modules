from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListAssessmentsRequest(BaseModel):
    ClusterArn: StrictStr
    AssessmentType: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
