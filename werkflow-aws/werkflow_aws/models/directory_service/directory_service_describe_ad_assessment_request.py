from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeADAssessmentRequest(BaseModel):
    AssessmentId: StrictStr
