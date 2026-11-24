from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_compliance_summary import ConfigServiceComplianceSummary


class ConfigServiceGetComplianceSummaryByConfigRuleResponse(BaseModel):
    ComplianceSummary: ConfigServiceComplianceSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
