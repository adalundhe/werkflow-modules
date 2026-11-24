from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_control_domain_insights import AuditManagerControlDomainInsights


class AuditManagerListControlDomainInsightsResponse(BaseModel):
    controlDomainInsights: list[AuditManagerControlDomainInsights] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
