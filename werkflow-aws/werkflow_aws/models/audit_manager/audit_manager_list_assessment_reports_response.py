from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_report_metadata import AuditManagerAssessmentReportMetadata


class AuditManagerListAssessmentReportsResponse(BaseModel):
    assessmentReports: list[AuditManagerAssessmentReportMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
