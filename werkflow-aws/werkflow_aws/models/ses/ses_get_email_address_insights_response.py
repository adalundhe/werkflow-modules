from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_mailbox_validation import SESMailboxValidation


class SESGetEmailAddressInsightsResponse(BaseModel):
    MailboxValidation: SESMailboxValidation | None = None
    ResponseMetadata: dict[str, Any] | None = None
