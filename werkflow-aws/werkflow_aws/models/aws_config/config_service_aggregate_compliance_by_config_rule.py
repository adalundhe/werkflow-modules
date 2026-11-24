from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_compliance import ConfigServiceCompliance


class ConfigServiceAggregateComplianceByConfigRule(BaseModel):
    ConfigRuleName: StrictStr | None = None
    Compliance: ConfigServiceCompliance | None = None
    AccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
