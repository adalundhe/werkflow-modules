from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingSendNotifyTextMessageResponse(BaseModel):
    MessageId: StrictStr | None = None
    TemplateId: StrictStr | None = None
    ResolvedMessageBody: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
