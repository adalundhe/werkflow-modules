from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class StatusUpdate(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    statusCategory: StrictStr | None = None
