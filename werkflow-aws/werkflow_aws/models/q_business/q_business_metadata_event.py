from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_source_attribution import QBusinessSourceAttribution


class QBusinessMetadataEvent(BaseModel):
    conversationId: StrictStr | None = None
    userMessageId: StrictStr | None = None
    systemMessageId: StrictStr | None = None
    sourceAttributions: list[QBusinessSourceAttribution] | None = None
    finalTextMessage: StrictStr | None = None
