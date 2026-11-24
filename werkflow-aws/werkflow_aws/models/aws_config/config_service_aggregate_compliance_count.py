from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_compliance_summary import ConfigServiceComplianceSummary


class ConfigServiceAggregateComplianceCount(BaseModel):
    GroupName: StrictStr | None = None
    ComplianceSummary: ConfigServiceComplianceSummary | None = None
