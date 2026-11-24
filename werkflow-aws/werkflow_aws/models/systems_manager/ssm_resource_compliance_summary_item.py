from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_compliance_execution_summary import SSMComplianceExecutionSummary
from .ssm_compliant_summary import SSMCompliantSummary
from .ssm_non_compliant_summary import SSMNonCompliantSummary


class SSMResourceComplianceSummaryItem(BaseModel):
    ComplianceType: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Status: StrictStr | None = None
    OverallSeverity: StrictStr | None = None
    ExecutionSummary: SSMComplianceExecutionSummary | None = None
    CompliantSummary: SSMCompliantSummary | None = None
    NonCompliantSummary: SSMNonCompliantSummary | None = None
