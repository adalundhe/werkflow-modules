from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_account_gate_result import CloudFormationAccountGateResult


class CloudFormationStackSetOperationResultSummary(BaseModel):
    Account: StrictStr | None = None
    Region: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    AccountGateResult: CloudFormationAccountGateResult | None = None
    OrganizationalUnitId: StrictStr | None = None
