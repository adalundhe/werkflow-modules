from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_push_message import PinpointJourneyPushMessage


class PinpointPushMessageActivity(BaseModel):
    MessageConfig: PinpointJourneyPushMessage | None = None
    NextActivity: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateVersion: StrictStr | None = None
