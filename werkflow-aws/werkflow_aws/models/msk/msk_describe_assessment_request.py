from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeAssessmentRequest(BaseModel):
    AssessmentArn: StrictStr
    ClusterArn: StrictStr
