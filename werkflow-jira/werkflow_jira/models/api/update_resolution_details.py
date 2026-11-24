from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class UpdateResolutionDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    name: StrictStr | None = None
