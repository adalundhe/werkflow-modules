from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class HistoryMetadataParticipant(BaseModel):
    model_config = ConfigDict(extra="allow")

    avatarUrl: StrictStr | None = None
    displayName: StrictStr | None = None
    displayNameKey: StrictStr | None = None
    id: StrictStr | None = None
    type: StrictStr | None = None
    url: StrictStr | None = None
