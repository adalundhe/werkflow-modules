from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFormationStackEvent(BaseModel):
    StackId: StrictStr | None = None
    EventId: StrictStr | None = None
    StackName: StrictStr | None = None
    OperationId: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    ResourceStatus: StrictStr | None = None
    ResourceStatusReason: StrictStr | None = None
    ResourceProperties: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    HookType: StrictStr | None = None
    HookStatus: StrictStr | None = None
    HookStatusReason: StrictStr | None = None
    HookInvocationPoint: StrictStr | None = None
    HookInvocationId: StrictStr | None = None
    HookFailureMode: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
