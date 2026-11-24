from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_framework_metadata import AuditManagerAssessmentFrameworkMetadata


class AuditManagerListAssessmentFrameworksResponse(BaseModel):
    frameworkMetadataList: list[AuditManagerAssessmentFrameworkMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
