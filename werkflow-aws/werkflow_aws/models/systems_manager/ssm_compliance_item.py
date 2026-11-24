from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_compliance_execution_summary import SSMComplianceExecutionSummary


class SSMComplianceItem(BaseModel):
    ComplianceType: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Id: StrictStr | None = None
    Title: StrictStr | None = None
    Status: StrictStr | None = None
    Severity: StrictStr | None = None
    ExecutionSummary: SSMComplianceExecutionSummary | None = None
    Details: dict[StrictStr, StrictStr] | None = None
