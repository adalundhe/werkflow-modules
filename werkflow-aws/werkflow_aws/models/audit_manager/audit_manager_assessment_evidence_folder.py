from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerAssessmentEvidenceFolder(BaseModel):
    name: StrictStr | None = None
    date: datetime.datetime | StrictStr | None = None
    assessmentId: StrictStr | None = None
    controlSetId: StrictStr | None = None
    controlId: StrictStr | None = None
    id: StrictStr | None = None
    dataSource: StrictStr | None = None
    author: StrictStr | None = None
    totalEvidence: StrictInt | None = None
    assessmentReportSelectionCount: StrictInt | None = None
    controlName: StrictStr | None = None
    evidenceResourcesIncludedCount: StrictInt | None = None
    evidenceByTypeConfigurationDataCount: StrictInt | None = None
    evidenceByTypeManualCount: StrictInt | None = None
    evidenceByTypeComplianceCheckCount: StrictInt | None = None
    evidenceByTypeComplianceCheckIssuesCount: StrictInt | None = None
    evidenceByTypeUserActivityCount: StrictInt | None = None
    evidenceAwsServiceSourceCount: StrictInt | None = None
