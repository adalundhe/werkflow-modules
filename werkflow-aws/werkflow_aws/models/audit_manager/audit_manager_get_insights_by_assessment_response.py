from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_insights_by_assessment import AuditManagerInsightsByAssessment


class AuditManagerGetInsightsByAssessmentResponse(BaseModel):
    insights: AuditManagerInsightsByAssessment | None = None
    ResponseMetadata: dict[str, Any] | None = None
