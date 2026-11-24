from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_conformance_pack_compliance import ConfigServiceAggregateConformancePackCompliance


class ConfigServiceAggregateComplianceByConformancePack(BaseModel):
    ConformancePackName: StrictStr | None = None
    Compliance: ConfigServiceAggregateConformancePackCompliance | None = None
    AccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
