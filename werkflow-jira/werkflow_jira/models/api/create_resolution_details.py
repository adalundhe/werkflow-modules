from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class CreateResolutionDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    name: StrictStr | None = None
