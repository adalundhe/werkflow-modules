from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_aws_account import AuditManagerAWSAccount
from .audit_manager_assessment_framework import AuditManagerAssessmentFramework
from .audit_manager_assessment_metadata import AuditManagerAssessmentMetadata


class AuditManagerAssessment(BaseModel):
    arn: StrictStr | None = None
    awsAccount: AuditManagerAWSAccount | None = None
    metadata: AuditManagerAssessmentMetadata | None = None
    framework: AuditManagerAssessmentFramework | None = None
    tags: dict[StrictStr, StrictStr] | None = None
