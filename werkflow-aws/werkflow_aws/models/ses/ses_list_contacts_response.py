from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_contact import SESContact


class SESListContactsResponse(BaseModel):
    Contacts: list[SESContact] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
