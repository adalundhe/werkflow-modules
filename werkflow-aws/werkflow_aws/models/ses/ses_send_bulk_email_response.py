from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_bulk_email_entry_result import SESBulkEmailEntryResult


class SESSendBulkEmailResponse(BaseModel):
    BulkEmailEntryResults: list[SESBulkEmailEntryResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
