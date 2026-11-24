from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_insights import AuditManagerInsights


class AuditManagerGetInsightsResponse(BaseModel):
    insights: AuditManagerInsights | None = None
    ResponseMetadata: dict[str, Any] | None = None
