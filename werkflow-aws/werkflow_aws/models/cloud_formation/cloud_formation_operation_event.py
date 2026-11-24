from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFormationOperationEvent(BaseModel):
    EventId: StrictStr | None = None
    StackId: StrictStr | None = None
    OperationId: StrictStr | None = None
    OperationType: StrictStr | None = None
    OperationStatus: StrictStr | None = None
    EventType: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResourceStatus: StrictStr | None = None
    ResourceStatusReason: StrictStr | None = None
    ResourceProperties: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    HookType: StrictStr | None = None
    HookStatus: StrictStr | None = None
    HookStatusReason: StrictStr | None = None
    HookInvocationPoint: StrictStr | None = None
    HookFailureMode: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    ValidationFailureMode: StrictStr | None = None
    ValidationName: StrictStr | None = None
    ValidationStatus: StrictStr | None = None
    ValidationStatusReason: StrictStr | None = None
    ValidationPath: StrictStr | None = None
