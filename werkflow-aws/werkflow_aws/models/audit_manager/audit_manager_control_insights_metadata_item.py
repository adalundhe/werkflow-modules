from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .audit_manager_evidence_insights import AuditManagerEvidenceInsights


class AuditManagerControlInsightsMetadataItem(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    evidenceInsights: AuditManagerEvidenceInsights | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
