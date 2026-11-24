from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .audit_manager_assessment_reports_destination import AuditManagerAssessmentReportsDestination
from .audit_manager_default_export_destination import AuditManagerDefaultExportDestination
from .audit_manager_deregistration_policy import AuditManagerDeregistrationPolicy
from .audit_manager_role import AuditManagerRole


class AuditManagerUpdateSettingsRequest(BaseModel):
    snsTopic: StrictStr | None = None
    defaultAssessmentReportsDestination: AuditManagerAssessmentReportsDestination | None = None
    defaultProcessOwners: list[AuditManagerRole] | None = None
    kmsKey: StrictStr | None = None
    evidenceFinderEnabled: StrictBool | None = None
    deregistrationPolicy: AuditManagerDeregistrationPolicy | None = None
    defaultExportDestination: AuditManagerDefaultExportDestination | None = None
