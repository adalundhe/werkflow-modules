from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudFormationRoleProvisioning(BaseModel):
    Status: StrictStr | None = None
    SucceededAccountsCount: StrictInt | None = None
    FailedAccountsCount: StrictInt | None = None
    CompletedAccountsCount: StrictInt | None = None
    PendingAccountsCount: StrictInt | None = None
    PercentageCompleted: StrictFloat | StrictInt | None = None
