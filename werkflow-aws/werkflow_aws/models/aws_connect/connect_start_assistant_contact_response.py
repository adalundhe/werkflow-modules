from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectStartAssistantContactResponse(BaseModel):
    ContactId: StrictStr | None = None
    ParticipantId: StrictStr | None = None
    ParticipantToken: StrictStr | None = None
    ContinuedFromContactId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
