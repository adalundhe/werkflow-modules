from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_framework_share_request import AuditManagerAssessmentFrameworkShareRequest


class AuditManagerListAssessmentFrameworkShareRequestsResponse(BaseModel):
    assessmentFrameworkShareRequests: list[AuditManagerAssessmentFrameworkShareRequest] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
