from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_message_header import PinpointMessageHeader


class PinpointCampaignEmailMessage(BaseModel):
    Body: StrictStr | None = None
    FromAddress: StrictStr | None = None
    Headers: list[PinpointMessageHeader] | None = None
    HtmlBody: StrictStr | None = None
    Title: StrictStr | None = None
