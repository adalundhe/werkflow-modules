from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .connect_media_concurrency import ConnectMediaConcurrency


class ConnectRoutingProfile(BaseModel):
    InstanceId: StrictStr | None = None
    Name: StrictStr | None = None
    RoutingProfileArn: StrictStr | None = None
    RoutingProfileId: StrictStr | None = None
    Description: StrictStr | None = None
    MediaConcurrencies: list[ConnectMediaConcurrency] | None = None
    DefaultOutboundQueueId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    NumberOfAssociatedQueues: StrictInt | None = None
    NumberOfAssociatedManualAssignmentQueues: StrictInt | None = None
    NumberOfAssociatedUsers: StrictInt | None = None
    AgentAvailabilityTimer: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    IsDefault: StrictBool | None = None
    AssociatedQueueIds: list[StrictStr] | None = None
    AssociatedManualAssignmentQueueIds: list[StrictStr] | None = None
