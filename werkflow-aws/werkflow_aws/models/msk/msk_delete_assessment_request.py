from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteAssessmentRequest(BaseModel):
    AssessmentArn: StrictStr
    ClusterArn: StrictStr
