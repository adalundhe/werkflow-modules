from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_event_destination import EndUserMessagingEventDestination


class EndUserMessagingConfigurationSetInformation(BaseModel):
    ConfigurationSetArn: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    EventDestinations: list[EndUserMessagingEventDestination] | None = None
    DefaultMessageType: StrictStr | None = None
    DefaultSenderId: StrictStr | None = None
    DefaultMessageFeedbackEnabled: StrictBool | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    ProtectConfigurationId: StrictStr | None = None
