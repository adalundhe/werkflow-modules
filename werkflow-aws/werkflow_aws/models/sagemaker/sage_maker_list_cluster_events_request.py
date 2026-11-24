from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListClusterEventsRequest(BaseModel):
    ClusterName: StrictStr
    InstanceGroupName: StrictStr | None = None
    NodeId: StrictStr | None = None
    EventTimeAfter: datetime.datetime | StrictStr | None = None
    EventTimeBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['EventTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    ResourceType: Literal['Cluster', 'InstanceGroup', 'Instance'] | None = None
    OperationId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
