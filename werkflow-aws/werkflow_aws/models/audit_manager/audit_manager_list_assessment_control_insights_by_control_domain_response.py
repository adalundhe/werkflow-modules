from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_control_insights_metadata_by_assessment_item import AuditManagerControlInsightsMetadataByAssessmentItem


class AuditManagerListAssessmentControlInsightsByControlDomainResponse(BaseModel):
    controlInsightsByAssessment: list[AuditManagerControlInsightsMetadataByAssessmentItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
