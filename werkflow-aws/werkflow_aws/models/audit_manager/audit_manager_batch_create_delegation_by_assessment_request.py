from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_create_delegation_request import AuditManagerCreateDelegationRequest


class AuditManagerBatchCreateDelegationByAssessmentRequest(BaseModel):
    createDelegationRequests: list[AuditManagerCreateDelegationRequest]
    assessmentId: StrictStr
