from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_metadata_item import AuditManagerAssessmentMetadataItem


class AuditManagerListAssessmentsResponse(BaseModel):
    assessmentMetadata: list[AuditManagerAssessmentMetadataItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
