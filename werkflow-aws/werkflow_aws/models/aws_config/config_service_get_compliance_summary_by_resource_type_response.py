from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_compliance_summary_by_resource_type import ConfigServiceComplianceSummaryByResourceType


class ConfigServiceGetComplianceSummaryByResourceTypeResponse(BaseModel):
    ComplianceSummariesByResourceType: list[ConfigServiceComplianceSummaryByResourceType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
