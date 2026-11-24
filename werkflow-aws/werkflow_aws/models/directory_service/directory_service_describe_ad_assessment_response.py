from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_assessment import DirectoryServiceAssessment
from .directory_service_assessment_report import DirectoryServiceAssessmentReport


class DirectoryServiceDescribeADAssessmentResponse(BaseModel):
    Assessment: DirectoryServiceAssessment | None = None
    AssessmentReports: list[DirectoryServiceAssessmentReport] | None = None
    ResponseMetadata: dict[str, Any] | None = None
