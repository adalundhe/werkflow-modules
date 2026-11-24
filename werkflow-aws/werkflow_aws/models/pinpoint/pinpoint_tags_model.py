from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointTagsModel(BaseModel):
    tags: dict[StrictStr, StrictStr] | None = None
