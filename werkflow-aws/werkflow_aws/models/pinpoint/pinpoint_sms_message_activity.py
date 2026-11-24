from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_sms_message import PinpointJourneySMSMessage


class PinpointSMSMessageActivity(BaseModel):
    MessageConfig: PinpointJourneySMSMessage | None = None
    NextActivity: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateVersion: StrictStr | None = None
