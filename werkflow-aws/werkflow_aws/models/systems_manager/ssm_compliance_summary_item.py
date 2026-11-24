from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_compliant_summary import SSMCompliantSummary
from .ssm_non_compliant_summary import SSMNonCompliantSummary


class SSMComplianceSummaryItem(BaseModel):
    ComplianceType: StrictStr | None = None
    CompliantSummary: SSMCompliantSummary | None = None
    NonCompliantSummary: SSMNonCompliantSummary | None = None
