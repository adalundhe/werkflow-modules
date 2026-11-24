from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_resource import AuditManagerResource


class AuditManagerEvidence(BaseModel):
    dataSource: StrictStr | None = None
    evidenceAwsAccountId: StrictStr | None = None
    time: datetime.datetime | StrictStr | None = None
    eventSource: StrictStr | None = None
    eventName: StrictStr | None = None
    evidenceByType: StrictStr | None = None
    resourcesIncluded: list[AuditManagerResource] | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    iamId: StrictStr | None = None
    complianceCheck: StrictStr | None = None
    awsOrganization: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    evidenceFolderId: StrictStr | None = None
    id: StrictStr | None = None
    assessmentReportSelection: StrictStr | None = None
