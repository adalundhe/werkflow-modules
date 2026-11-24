from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppAssessmentRequest(BaseModel):
    assessmentArn: StrictStr
