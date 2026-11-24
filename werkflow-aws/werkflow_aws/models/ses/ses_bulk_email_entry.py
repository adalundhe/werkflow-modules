from __future__ import annotations
from pydantic import BaseModel
from .ses_destination import SESDestination
from .ses_message_header import SESMessageHeader
from .ses_message_tag import SESMessageTag
from .ses_replacement_email_content import SESReplacementEmailContent


class SESBulkEmailEntry(BaseModel):
    Destination: SESDestination
    ReplacementTags: list[SESMessageTag] | None = None
    ReplacementEmailContent: SESReplacementEmailContent | None = None
    ReplacementHeaders: list[SESMessageHeader] | None = None
