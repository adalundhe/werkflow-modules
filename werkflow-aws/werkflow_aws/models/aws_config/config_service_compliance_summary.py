from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_compliance_contributor_count import ConfigServiceComplianceContributorCount


class ConfigServiceComplianceSummary(BaseModel):
    CompliantResourceCount: ConfigServiceComplianceContributorCount | None = None
    NonCompliantResourceCount: ConfigServiceComplianceContributorCount | None = None
    ComplianceSummaryTimestamp: datetime.datetime | StrictStr | None = None
