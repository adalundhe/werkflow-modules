from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_email_message import PinpointJourneyEmailMessage


class PinpointEmailMessageActivity(BaseModel):
    MessageConfig: PinpointJourneyEmailMessage | None = None
    NextActivity: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateVersion: StrictStr | None = None
