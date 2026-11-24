from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_event_filter import CloudFormationEventFilter


class CloudFormationDescribeEventsRequest(BaseModel):
    StackName: StrictStr | None = None
    ChangeSetName: StrictStr | None = None
    OperationId: StrictStr | None = None
    Filters: CloudFormationEventFilter | None = None
    NextToken: StrictStr | None = None
