from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_control_insights_metadata_item import AuditManagerControlInsightsMetadataItem


class AuditManagerListControlInsightsByControlDomainResponse(BaseModel):
    controlInsightsMetadata: list[AuditManagerControlInsightsMetadataItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
