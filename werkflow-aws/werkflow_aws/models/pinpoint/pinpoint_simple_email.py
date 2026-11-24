from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_message_header import PinpointMessageHeader
from .pinpoint_simple_email_part import PinpointSimpleEmailPart


class PinpointSimpleEmail(BaseModel):
    HtmlPart: PinpointSimpleEmailPart | None = None
    Subject: PinpointSimpleEmailPart | None = None
    TextPart: PinpointSimpleEmailPart | None = None
    Headers: list[PinpointMessageHeader] | None = None
