from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudFormationStackInstancesDeployment(BaseModel):
    Status: StrictStr | None = None
    SucceededStackInstancesCount: StrictInt | None = None
    FailedStackInstancesCount: StrictInt | None = None
    CompletedStackInstancesCount: StrictInt | None = None
    PendingStackInstancesCount: StrictInt | None = None
    CancelledStackInstancesCount: StrictInt | None = None
    SkippedStackInstancesCount: StrictInt | None = None
    PercentageCompleted: StrictFloat | StrictInt | None = None
