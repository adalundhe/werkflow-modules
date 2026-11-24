from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_create_delegation_request import AuditManagerCreateDelegationRequest


class AuditManagerBatchCreateDelegationByAssessmentError(BaseModel):
    createDelegationRequest: AuditManagerCreateDelegationRequest | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
