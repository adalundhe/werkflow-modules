from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_compliance_contributor_count import ConfigServiceComplianceContributorCount


class ConfigServiceCompliance(BaseModel):
    ComplianceType: StrictStr | None = None
    ComplianceContributorCount: ConfigServiceComplianceContributorCount | None = None
