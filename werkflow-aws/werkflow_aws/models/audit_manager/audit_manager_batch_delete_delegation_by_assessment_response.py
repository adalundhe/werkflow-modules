from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_batch_delete_delegation_by_assessment_error import AuditManagerBatchDeleteDelegationByAssessmentError


class AuditManagerBatchDeleteDelegationByAssessmentResponse(BaseModel):
    errors: list[AuditManagerBatchDeleteDelegationByAssessmentError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
