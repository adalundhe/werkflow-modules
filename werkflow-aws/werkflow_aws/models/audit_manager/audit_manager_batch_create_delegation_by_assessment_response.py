from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_batch_create_delegation_by_assessment_error import AuditManagerBatchCreateDelegationByAssessmentError
from .audit_manager_delegation import AuditManagerDelegation


class AuditManagerBatchCreateDelegationByAssessmentResponse(BaseModel):
    delegations: list[AuditManagerDelegation] | None = None
    errors: list[AuditManagerBatchCreateDelegationByAssessmentError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
