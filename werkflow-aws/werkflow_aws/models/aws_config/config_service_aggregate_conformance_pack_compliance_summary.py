from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_conformance_pack_compliance_count import ConfigServiceAggregateConformancePackComplianceCount


class ConfigServiceAggregateConformancePackComplianceSummary(BaseModel):
    ComplianceSummary: ConfigServiceAggregateConformancePackComplianceCount | None = None
    GroupName: StrictStr | None = None
