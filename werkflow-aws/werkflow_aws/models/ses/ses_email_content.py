from __future__ import annotations
from pydantic import BaseModel
from .ses_message import SESMessage
from .ses_raw_message import SESRawMessage
from .ses_template import SESTemplate


class SESEmailContent(BaseModel):
    Simple: SESMessage | None = None
    Raw: SESRawMessage | None = None
    Template: SESTemplate | None = None
