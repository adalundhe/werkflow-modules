from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_messaging_limits import EndUserMessagingMessagingLimits
from .end_user_messaging_testing_agent_information import EndUserMessagingTestingAgentInformation


class EndUserMessagingRcsAgentInformation(BaseModel):
    RcsAgentArn: StrictStr | None = None
    RcsAgentId: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    OptOutListName: StrictStr | None = None
    SelfManagedOptOutsEnabled: StrictBool | None = None
    TwoWayChannelArn: StrictStr | None = None
    TwoWayChannelRole: StrictStr | None = None
    TwoWayEnabled: StrictBool | None = None
    PoolId: StrictStr | None = None
    TwoWayMediaS3BucketName: StrictStr | None = None
    TwoWayMediaS3KeyPrefix: StrictStr | None = None
    TwoWayMediaS3Role: StrictStr | None = None
    TwoWayRcsEventsEnabled: list[StrictStr] | None = None
    TestingAgent: EndUserMessagingTestingAgentInformation | None = None
    MessagingLimits: EndUserMessagingMessagingLimits | None = None
