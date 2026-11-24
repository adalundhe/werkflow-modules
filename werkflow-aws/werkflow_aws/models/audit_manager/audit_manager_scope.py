from __future__ import annotations
from pydantic import BaseModel
from .audit_manager_aws_account import AuditManagerAWSAccount
from .audit_manager_aws_service import AuditManagerAWSService


class AuditManagerScope(BaseModel):
    awsAccounts: list[AuditManagerAWSAccount] | None = None
    awsServices: list[AuditManagerAWSService] | None = None
