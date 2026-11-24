from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_custom_message import PinpointJourneyCustomMessage


class PinpointCustomMessageActivity(BaseModel):
    DeliveryUri: StrictStr | None = None
    EndpointTypes: list[StrictStr] | None = None
    MessageConfig: PinpointJourneyCustomMessage | None = None
    NextActivity: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateVersion: StrictStr | None = None
