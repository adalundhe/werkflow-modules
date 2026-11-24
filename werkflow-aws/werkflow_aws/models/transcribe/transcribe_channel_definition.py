from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeChannelDefinition(BaseModel):
    ChannelId: StrictInt | None = None
    ParticipantRole: StrictStr | None = None
