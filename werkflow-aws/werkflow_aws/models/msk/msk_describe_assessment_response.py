from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_assessment_parameters import MSKAssessmentParameters
from .msk_assessment_summary import MSKAssessmentSummary


class MSKDescribeAssessmentResponse(BaseModel):
    AssessmentArn: StrictStr | None = None
    AssessmentParameters: MSKAssessmentParameters | None = None
    AssessmentType: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Summary: MSKAssessmentSummary | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
