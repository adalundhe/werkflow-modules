from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_event_destination import EndUserMessagingEventDestination


class EndUserMessagingDeleteEventDestinationResponse(BaseModel):
    ConfigurationSetArn: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    EventDestination: EndUserMessagingEventDestination | None = None
    ResponseMetadata: dict[str, Any] | None = None
