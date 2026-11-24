from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_event_details import SageMakerEventDetails


class SageMakerClusterEventDetail(BaseModel):
    EventId: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    InstanceGroupName: StrictStr | None = None
    InstanceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    EventTime: datetime.datetime | StrictStr | None = None
    EventDetails: SageMakerEventDetails | None = None
    Description: StrictStr | None = None
    EventLevel: StrictStr | None = None
    OperationId: StrictStr | None = None
