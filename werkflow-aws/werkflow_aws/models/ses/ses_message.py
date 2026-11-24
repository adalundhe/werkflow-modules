from __future__ import annotations
from pydantic import BaseModel
from .ses_attachment import SESAttachment
from .ses_body import SESBody
from .ses_content import SESContent
from .ses_message_header import SESMessageHeader


class SESMessage(BaseModel):
    Subject: SESContent
    Body: SESBody
    Headers: list[SESMessageHeader] | None = None
    Attachments: list[SESAttachment] | None = None
