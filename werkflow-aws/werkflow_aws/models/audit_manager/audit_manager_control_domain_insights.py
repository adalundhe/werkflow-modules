from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .audit_manager_evidence_insights import AuditManagerEvidenceInsights


class AuditManagerControlDomainInsights(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    controlsCountByNoncompliantEvidence: StrictInt | None = None
    totalControlsCount: StrictInt | None = None
    evidenceInsights: AuditManagerEvidenceInsights | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
