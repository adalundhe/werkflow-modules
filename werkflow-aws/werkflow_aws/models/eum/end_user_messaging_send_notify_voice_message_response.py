from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingSendNotifyVoiceMessageResponse(BaseModel):
    MessageId: StrictStr | None = None
    TemplateId: StrictStr | None = None
    ResolvedMessageBody: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
