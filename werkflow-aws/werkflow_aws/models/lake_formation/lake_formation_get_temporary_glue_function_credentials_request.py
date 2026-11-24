from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_audit_context import LakeFormationAuditContext


class LakeFormationGetTemporaryGlueFunctionCredentialsRequest(BaseModel):
    UserDefinedFunctionArn: StrictStr
    AuditContext: LakeFormationAuditContext | None = None
