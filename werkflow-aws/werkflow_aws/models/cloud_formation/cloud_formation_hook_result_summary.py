from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFormationHookResultSummary(BaseModel):
    HookResultId: StrictStr | None = None
    InvocationPoint: StrictStr | None = None
    FailureMode: StrictStr | None = None
    TypeName: StrictStr | None = None
    TypeVersionId: StrictStr | None = None
    TypeConfigurationVersionId: StrictStr | None = None
    Status: StrictStr | None = None
    HookStatusReason: StrictStr | None = None
    InvokedAt: datetime.datetime | StrictStr | None = None
    TargetType: StrictStr | None = None
    TargetId: StrictStr | None = None
    TypeArn: StrictStr | None = None
    HookExecutionTarget: StrictStr | None = None
