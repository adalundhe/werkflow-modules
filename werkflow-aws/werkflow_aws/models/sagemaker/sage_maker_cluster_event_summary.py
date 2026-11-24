from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerClusterEventSummary(BaseModel):
    EventId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    InstanceGroupName: StrictStr | None = None
    InstanceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    EventTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    EventLevel: StrictStr | None = None
    OperationId: StrictStr | None = None
