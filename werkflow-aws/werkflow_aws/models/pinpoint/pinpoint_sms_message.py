from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class PinpointSMSMessage(BaseModel):
    Body: StrictStr | None = None
    Keyword: StrictStr | None = None
    MediaUrl: StrictStr | None = None
    MessageType: Literal['TRANSACTIONAL', 'PROMOTIONAL'] | None = None
    OriginationNumber: StrictStr | None = None
    SenderId: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    EntityId: StrictStr | None = None
    TemplateId: StrictStr | None = None
