from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class ResolutionId(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: StrictStr | None = None
