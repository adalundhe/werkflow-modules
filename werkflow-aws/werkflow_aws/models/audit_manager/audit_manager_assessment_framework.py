from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_control_set import AuditManagerAssessmentControlSet
from .audit_manager_framework_metadata import AuditManagerFrameworkMetadata


class AuditManagerAssessmentFramework(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    metadata: AuditManagerFrameworkMetadata | None = None
    controlSets: list[AuditManagerAssessmentControlSet] | None = None
