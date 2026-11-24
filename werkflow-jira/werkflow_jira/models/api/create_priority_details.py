from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr


class CreatePriorityDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    avatarId: StrictInt | None = None
    description: StrictStr | None = None
    iconUrl: StrictStr | None = None
    name: StrictStr | None = None
    statusColor: StrictStr | None = None
