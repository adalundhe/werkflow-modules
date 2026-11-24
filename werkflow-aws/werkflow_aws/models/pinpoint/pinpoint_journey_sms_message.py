from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneySMSMessage(BaseModel):
    MessageType: StrictStr | None = None
    OriginationNumber: StrictStr | None = None
    SenderId: StrictStr | None = None
    EntityId: StrictStr | None = None
    TemplateId: StrictStr | None = None
