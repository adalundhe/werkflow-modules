from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_blacklist_entry import SESBlacklistEntry


class SESGetBlacklistReportsResponse(BaseModel):
    BlacklistReport: dict[StrictStr, list[SESBlacklistEntry]] | None = None
    ResponseMetadata: dict[str, Any] | None = None
